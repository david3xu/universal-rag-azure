# Getting Started - TODO-Driven Development

**🚧 Current State: TODO-Driven Development Phase**

## Table of Contents

- [Current Status](#current-status)
- [Development Setup](#development-setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Development Approach](#development-approach)
  - [⚠️ Important: Current State](#️-important-current-state)
  - [Step-by-Step Implementation](#step-by-step-implementation)
- [What You'll Find](#what-youll-find)
  - [In Each File](#in-each-file)
  - [Pre-commit Hook Protection](#pre-commit-hook-protection)
- [Current Architecture State](#current-architecture-state)
  - [✅ Ready for Implementation](#-ready-for-implementation)
  - [🔄 Implementation Order (Recommended)](#-implementation-order-recommended)
- [Development Guidelines](#development-guidelines)
  - [Zero-Hardcoded-Values Principle](#zero-hardcoded-values-principle)
  - [TODO-Driven Implementation](#todo-driven-implementation)
- [Testing Your Implementation](#testing-your-implementation)
- [Next Steps](#next-steps)
- [Need Help?](#need-help)

## Current Status

**⚠️ This project is in TODO-driven development phase**

All implementation has been systematically cleaned to provide comprehensive development guidance through TODOs. The system cannot run until TODOs are implemented.

## Development Setup

### Prerequisites
- Python 3.9+
- Azure subscription (for service integration)
- Git with pre-commit hooks support

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd universal-rag-azure
   ```

2. **Install development dependencies**
   ```bash
   pip install -r requirements.txt
   pip install pre-commit
   ```

3. **Set up pre-commit hooks** (enforces zero-hardcoded-values)
   ```bash
   pre-commit install
   ```

4. **Verify cleanup state**
   ```bash
   # All files should contain only TODOs and pass statements
   find . -name "*.py" -exec grep -l "TODO" {} \;
   ```

## Development Approach

### ⚠️ Important: Current State
- **API will NOT start** until TODOs are implemented
- **All endpoints return TODO placeholders**
- **All agents contain only TODO guidance**
- **All Azure services are TODO-driven**

### Step-by-Step Implementation

1. **Choose a starting component** (recommended: `agents/supports/`)
   ```bash
   # Example: Start with ConfigProvider
   cd agents/supports/
   cat config_provider.py  # Review TODOs
   ```

2. **Implement following TODOs**
   - Replace `pass` statements with actual implementation
   - Follow zero-hardcoded-values principle
   - Use only learned/provided configuration

3. **Test against pre-commit hooks**
   ```bash
   git add .
   git commit -m "Implement ConfigProvider basic functionality"
   # Pre-commit hooks will enforce zero-hardcoded-values
   ```

4. **Move to next component**
   - Follow dependency order (supports → auto_domain → gen_knowledge → uni_search)

## What You'll Find

### In Each File:
```python
# Example of current state:
class ConfigProvider:
    def __init__(self):
        # TODO: Initialize config provider with zero hardcoded values
        # TODO: Set up Azure service connections
        pass
    
    async def get_config(self, domain: str) -> Dict[str, Any]:
        # TODO: Load configuration for domain
        # TODO: Return learned configuration without fallbacks
        pass
```

### Pre-commit Hook Protection:
- Detects hardcoded values like `temperature = 0.7`
- Blocks commits with enum values like `TECHNICAL = "technical"`
- Prevents Pydantic field definitions until implemented
- Enforces comprehensive TODO documentation

## Current Architecture State

### ✅ Ready for Implementation
- **agents/supports/** - Configuration and workflow bridges
- **agents/auto_domain/** - Domain analysis and configuration generation
- **agents/gen_knowledge/** - Knowledge extraction workflows
- **agents/uni_search/** - Tri-modal search operations
- **api/** - FastAPI endpoints and application
- **prompt_flows/** - YAML-driven prompt orchestration
- **azure_services/** - Azure service integrations

### 🔄 Implementation Order (Recommended)
1. `agents/supports/config_provider.py` - Core configuration
2. `agents/supports/error_handler.py` - Error handling
3. `azure_services/` - Service clients
4. `agents/auto_domain/` - Domain configuration
5. `api/` - API endpoints
6. `agents/uni_search/` - Search operations
7. `prompt_flows/` - Advanced workflows

## Development Guidelines

### Zero-Hardcoded-Values Principle
```python
# ❌ Wrong - hardcoded values
similarity_threshold = 0.8
temperature = 0.7

# ✅ Correct - learned/provided configuration
config = await self.config_provider.get_config(domain)
similarity_threshold = config.get("similarity_threshold")
temperature = config.get("llm_temperature")
```

### TODO-Driven Implementation
```python
# Each TODO provides specific implementation guidance
# TODO: Load Azure OpenAI client with endpoint from config
# TODO: Use config.azure_openai_endpoint - NO hardcoded fallback
# TODO: Configure client with learned parameters only
```

## Testing Your Implementation

### Verify No Hardcoded Values
```bash
# Pre-commit hooks will catch hardcoded values
git add .
git commit -m "Test implementation"
```

### Run Basic Functionality Tests
```bash
# Once basic components are implemented
python -c "from agents.supports.config_provider import ConfigProvider; print('✅ Import successful')"
```

## Next Steps

1. **Start with configuration components** (`agents/supports/`)
2. **Follow TODO guidance** in each file
3. **Maintain zero-hardcoded-values** principle
4. **Test with pre-commit hooks** before committing
5. **Build incrementally** following dependency order

## Need Help?

- Review TODO comments in source files
- Check pre-commit hook messages for guidance
- Follow the architecture documents in `docs/architecture/`
- Each TODO explains exactly what needs to be implemented
