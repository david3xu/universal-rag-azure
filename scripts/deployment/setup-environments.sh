#\!/bin/bash
# Setup script for different environments

echo "🔧 Setting up Universal RAG environments..."

# Function to setup environment
setup_env() {
    local env=$1
    echo "Setting up $env environment..."
    
    # Copy environment file
    if [ -f "config/environments/${env}.env" ]; then
        cp "config/environments/${env}.env" .env
        echo "✅ Environment file copied for $env"
    else
        echo "❌ Environment file not found for $env"
        exit 1
    fi
}

# Check argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <environment>"
    echo "Available environments: development, staging"
    exit 1
fi

# Setup specified environment
setup_env $1

echo "✅ Environment setup completed for $1"
