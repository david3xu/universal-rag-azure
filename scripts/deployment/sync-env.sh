#!/bin/bash
# Environment Synchronization Script
# Synchronizes Azure environment configuration with azd environment selection

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
ENVIRONMENT=""
SYNC_BACKEND=true
VALIDATE_CONFIG=true
UPDATE_SECRETS=true

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_step() {
    echo -e "${BLUE}[STEP]${NC} $1"
}

# Function to show usage
show_usage() {
    cat << EOF
Environment Synchronization Script

Usage: $0 [environment] [options]

Arguments:
  environment    Target environment (development, staging, production)

Options:
  --no-backend   Skip backend configuration sync
  --no-validate  Skip configuration validation
  --no-secrets   Skip secret synchronization
  --help         Show this help message

Examples:
  $0 development              # Sync to development environment
  $0 staging --no-secrets     # Sync to staging without secrets
  $0 production --no-backend  # Sync to production without backend sync

EOF
}

# Function to validate environment
validate_environment() {
    local env=$1
    case $env in
        development|staging|production)
            return 0
            ;;
        *)
            print_error "Invalid environment: $env"
            print_error "Valid environments: development, staging, production"
            return 1
            ;;
    esac
}

# Function to check prerequisites
check_prerequisites() {
    print_step "Checking prerequisites..."
    
    # Check Azure CLI
    if ! command -v az &> /dev/null; then
        print_error "Azure CLI not found. Please install Azure CLI."
        exit 1
    fi
    
    # Check azd CLI
    if ! command -v azd &> /dev/null; then
        print_error "Azure Developer CLI (azd) not found. Please install azd."
        exit 1
    fi
    
    # Check if logged in to Azure
    if ! az account show &> /dev/null; then
        print_error "Not logged in to Azure. Please run 'az login' first."
        exit 1
    fi
    
    # Check if azd environment is initialized
    if ! azd env list &> /dev/null; then
        print_warning "No azd environments found. Run 'azd init' first."
    fi
    
    print_status "Prerequisites check passed"
}

# Function to sync azd environment
sync_azd_environment() {
    local target_env=$1
    
    print_step "Syncing azd environment to: $target_env"
    
    # Check if target environment exists
    if azd env list | grep -q "$target_env"; then
        print_status "Switching to existing azd environment: $target_env"
        azd env select "$target_env"
    else
        print_warning "Environment '$target_env' not found in azd"
        print_status "Creating new azd environment: $target_env"
        azd env new "$target_env"
    fi
    
    # Get current azd environment
    current_env=$(azd env get-values | grep AZURE_ENV_NAME | cut -d'=' -f2 | tr -d '"')
    if [ "$current_env" = "$target_env" ]; then
        print_status "Successfully switched to azd environment: $target_env"
    else
        print_error "Failed to switch to azd environment: $target_env"
        exit 1
    fi
}

# Function to sync backend configuration
sync_backend_config() {
    local target_env=$1
    
    if [ "$SYNC_BACKEND" = false ]; then
        print_step "Skipping backend configuration sync"
        return 0
    fi
    
    print_step "Syncing backend configuration for: $target_env"
    
    # Get azd environment values
    local azd_values_file=$(mktemp)
    azd env get-values > "$azd_values_file"
    
    # Extract Azure resource information
    local subscription_id=$(grep AZURE_SUBSCRIPTION_ID "$azd_values_file" | cut -d'=' -f2 | tr -d '"' || echo "")
    local resource_group=$(grep AZURE_RESOURCE_GROUP "$azd_values_file" | cut -d'=' -f2 | tr -d '"' || echo "")
    local location=$(grep AZURE_LOCATION "$azd_values_file" | cut -d'=' -f2 | tr -d '"' || echo "")
    
    # Create or update environment configuration
    local env_file="config/environments/${target_env}.env"
    
    print_status "Updating environment file: $env_file"
    
    # Backup existing file if it exists
    if [ -f "$env_file" ]; then
        cp "$env_file" "${env_file}.backup.$(date +%s)"
        print_status "Backed up existing configuration"
    fi
    
    # Create directory if it doesn't exist
    mkdir -p "config/environments"
    
    # Generate environment configuration
    cat > "$env_file" << EOF
# Azure Environment Configuration - $target_env
# Generated on $(date)
# Synchronized with azd environment: $target_env

# Core Azure Configuration
AZURE_SUBSCRIPTION_ID="$subscription_id"
AZURE_RESOURCE_GROUP="$resource_group"
AZURE_LOCATION="$location"
ENVIRONMENT="$target_env"

# Azure Service Endpoints (will be populated by azd)
AZURE_OPENAI_ENDPOINT=""
AZURE_SEARCH_ENDPOINT=""
AZURE_COSMOS_ENDPOINT=""
AZURE_STORAGE_ACCOUNT=""
AZURE_ML_WORKSPACE=""

# Authentication Configuration
USE_MANAGED_IDENTITY="true"
AZURE_CLIENT_ID=""

# Application Configuration
LOG_LEVEL="INFO"
DEBUG_MODE="false"
CACHE_TTL_SECONDS="3600"
MAX_CONCURRENT_REQUESTS="10"

# Performance Configuration
MAX_RESPONSE_TIME="3.0"
MIN_RELEVANCE_SCORE="0.8"
DEFAULT_MAX_RESULTS="10"

EOF
    
    # Clean up temporary file
    rm "$azd_values_file"
    
    print_status "Backend configuration synced successfully"
}

# Function to update Azure service endpoints
update_service_endpoints() {
    local target_env=$1
    local env_file="config/environments/${target_env}.env"
    
    print_step "Updating Azure service endpoints..."
    
    # Get current subscription and resource group
    local current_subscription=$(az account show --query id -o tsv)
    local resource_group=$(grep AZURE_RESOURCE_GROUP "$env_file" | cut -d'=' -f2 | tr -d '"')
    
    if [ -z "$resource_group" ]; then
        print_warning "Resource group not found in configuration"
        return 0
    fi
    
    print_status "Querying Azure resources in resource group: $resource_group"
    
    # Query Azure OpenAI endpoint
    local openai_endpoint=$(az cognitiveservices account show \
        --resource-group "$resource_group" \
        --name "$(az cognitiveservices account list -g "$resource_group" --query "[?kind=='OpenAI'].name" -o tsv | head -1)" \
        --query properties.endpoint -o tsv 2>/dev/null || echo "")
    
    # Query Azure Search endpoint
    local search_endpoint=$(az search service show \
        --resource-group "$resource_group" \
        --name "$(az search service list -g "$resource_group" --query "[0].name" -o tsv)" \
        --query hostName -o tsv 2>/dev/null || echo "")
    if [ -n "$search_endpoint" ]; then
        search_endpoint="https://$search_endpoint"
    fi
    
    # Query Azure Cosmos endpoint
    local cosmos_endpoint=$(az cosmosdb show \
        --resource-group "$resource_group" \
        --name "$(az cosmosdb list -g "$resource_group" --query "[0].name" -o tsv)" \
        --query documentEndpoint -o tsv 2>/dev/null || echo "")
    
    # Query Azure Storage account
    local storage_account=$(az storage account list \
        --resource-group "$resource_group" \
        --query "[0].name" -o tsv 2>/dev/null || echo "")
    
    # Query Azure ML workspace
    local ml_workspace=$(az ml workspace list \
        --resource-group "$resource_group" \
        --query "[0].name" -o tsv 2>/dev/null || echo "")
    
    # Update environment file with discovered endpoints
    if [ -n "$openai_endpoint" ]; then
        sed -i "s|AZURE_OPENAI_ENDPOINT=\".*\"|AZURE_OPENAI_ENDPOINT=\"$openai_endpoint\"|" "$env_file"
        print_status "Updated Azure OpenAI endpoint"
    fi
    
    if [ -n "$search_endpoint" ]; then
        sed -i "s|AZURE_SEARCH_ENDPOINT=\".*\"|AZURE_SEARCH_ENDPOINT=\"$search_endpoint\"|" "$env_file"
        print_status "Updated Azure Search endpoint"
    fi
    
    if [ -n "$cosmos_endpoint" ]; then
        sed -i "s|AZURE_COSMOS_ENDPOINT=\".*\"|AZURE_COSMOS_ENDPOINT=\"$cosmos_endpoint\"|" "$env_file"
        print_status "Updated Azure Cosmos endpoint"
    fi
    
    if [ -n "$storage_account" ]; then
        sed -i "s|AZURE_STORAGE_ACCOUNT=\".*\"|AZURE_STORAGE_ACCOUNT=\"$storage_account\"|" "$env_file"
        print_status "Updated Azure Storage account"
    fi
    
    if [ -n "$ml_workspace" ]; then
        sed -i "s|AZURE_ML_WORKSPACE=\".*\"|AZURE_ML_WORKSPACE=\"$ml_workspace\"|" "$env_file"
        print_status "Updated Azure ML workspace"
    fi
}

# Function to validate configuration
validate_configuration() {
    local target_env=$1
    
    if [ "$VALIDATE_CONFIG" = false ]; then
        print_step "Skipping configuration validation"
        return 0
    fi
    
    print_step "Validating configuration for: $target_env"
    
    local env_file="config/environments/${target_env}.env"
    
    if [ ! -f "$env_file" ]; then
        print_error "Environment file not found: $env_file"
        return 1
    fi
    
    # Check required variables
    local required_vars=("AZURE_SUBSCRIPTION_ID" "AZURE_RESOURCE_GROUP" "AZURE_LOCATION")
    local validation_errors=0
    
    for var in "${required_vars[@]}"; do
        if ! grep -q "^${var}=" "$env_file" || grep -q "^${var}=\"\"$" "$env_file"; then
            print_error "Required variable $var is missing or empty in $env_file"
            validation_errors=$((validation_errors + 1))
        fi
    done
    
    # Validate Azure connectivity
    print_status "Testing Azure connectivity..."
    
    if az account show &> /dev/null; then
        print_status "Azure CLI connectivity: OK"
    else
        print_error "Azure CLI connectivity: FAILED"
        validation_errors=$((validation_errors + 1))
    fi
    
    if [ $validation_errors -eq 0 ]; then
        print_status "Configuration validation passed"
        return 0
    else
        print_error "Configuration validation failed with $validation_errors errors"
        return 1
    fi
}

# Function to sync secrets (placeholder)
sync_secrets() {
    local target_env=$1
    
    if [ "$UPDATE_SECRETS" = false ]; then
        print_step "Skipping secret synchronization"
        return 0
    fi
    
    print_step "Synchronizing secrets for: $target_env"
    
    # TODO: Implement secret synchronization with Azure Key Vault
    # This would typically involve:
    # 1. Connecting to Azure Key Vault for the environment
    # 2. Retrieving necessary secrets (API keys, connection strings, etc.)
    # 3. Updating local environment file or secure storage
    # 4. Validating secret accessibility
    
    print_status "Secret synchronization completed (placeholder)"
}

# Function to generate summary
generate_summary() {
    local target_env=$1
    
    print_step "Environment synchronization summary"
    echo
    echo "Target Environment: $target_env"
    echo "Backend Sync: $([ "$SYNC_BACKEND" = true ] && echo "✓ Enabled" || echo "✗ Disabled")"
    echo "Configuration Validation: $([ "$VALIDATE_CONFIG" = true ] && echo "✓ Enabled" || echo "✗ Disabled")"
    echo "Secret Sync: $([ "$UPDATE_SECRETS" = true ] && echo "✓ Enabled" || echo "✗ Disabled")"
    echo
    echo "Configuration file: config/environments/${target_env}.env"
    echo "Azure subscription: $(az account show --query name -o tsv 2>/dev/null || echo "Unknown")"
    echo "Current azd environment: $(azd env get-values | grep AZURE_ENV_NAME | cut -d'=' -f2 | tr -d '"' 2>/dev/null || echo "Unknown")"
    echo
    print_status "Environment synchronization completed successfully!"
}

# Main execution
main() {
    # Parse command line arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --no-backend)
                SYNC_BACKEND=false
                shift
                ;;
            --no-validate)
                VALIDATE_CONFIG=false
                shift
                ;;
            --no-secrets)
                UPDATE_SECRETS=false
                shift
                ;;
            --help)
                show_usage
                exit 0
                ;;
            -*)
                print_error "Unknown option: $1"
                show_usage
                exit 1
                ;;
            *)
                if [ -z "$ENVIRONMENT" ]; then
                    ENVIRONMENT=$1
                else
                    print_error "Multiple environments specified"
                    show_usage
                    exit 1
                fi
                shift
                ;;
        esac
    done
    
    # Check if environment is specified
    if [ -z "$ENVIRONMENT" ]; then
        print_error "Environment not specified"
        show_usage
        exit 1
    fi
    
    # Validate environment
    if ! validate_environment "$ENVIRONMENT"; then
        exit 1
    fi
    
    # Execute synchronization steps
    check_prerequisites
    sync_azd_environment "$ENVIRONMENT"
    sync_backend_config "$ENVIRONMENT"
    update_service_endpoints "$ENVIRONMENT"
    validate_configuration "$ENVIRONMENT"
    sync_secrets "$ENVIRONMENT"
    generate_summary "$ENVIRONMENT"
}

# Run main function
main "$@"