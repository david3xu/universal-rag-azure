# Development Guide - TODO-Driven Implementation

**🚧 Current State: TODO-Driven Development Phase**

## Table of Contents

- [Current Status](#current-status)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [1. Environment Setup](#1-environment-setup)
  - [2. Azure Configuration](#2-azure-configuration)
  - [3. Environment Variables](#3-environment-variables)
- [TODO-Driven Development Workflow](#todo-driven-development-workflow)
  - [1. Current Implementation State](#1-current-implementation-state)
  - [2. Architecture Principles (Design Goals)](#2-architecture-principles-design-goals)
  - [3. Implementation Approach](#3-implementation-approach)
  - [4. Configuration Management (TODO-Guided)](#4-configuration-management-todo-guided)
  - [4. Prompt Flow Development](#4-prompt-flow-development)
  - [5. Testing Guidelines](#5-testing-guidelines)
  - [6. Performance Optimization](#6-performance-optimization)
- [Code Quality Standards](#code-quality-standards)
  - [1. Anti-Hardcoding Enforcement](#1-anti-hardcoding-enforcement)
  - [2. Centralized Data Types](#2-centralized-data-types)
  - [3. Type Safety](#3-type-safety)
  - [4. Error Handling](#4-error-handling)
- [Debugging and Troubleshooting](#debugging-and-troubleshooting)
- [Deployment](#deployment)
- [Best Practices](#best-practices)
- [Contributing](#contributing)
- [Resources](#resources)

## Current Status

**⚠️ All implementation has been systematically cleaned to TODO-only state**

This guide walks you through developing with the Azure Intelligent RAG dual-graph system in its current **TODO-driven development phase**. All code has been cleaned to provide comprehensive implementation guidance through TODOs.

## Prerequisites

- Python 3.11+
- Azure CLI
- Azure subscription with required services
- Git

## Setup Instructions

### 1. Environment Setup

```bash
# Clone and navigate to project
cd universal-rag-azure

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install pre-commit hooks (enforces zero-hardcoded-values)
pip install pre-commit
pre-commit install
```

### 2. Azure Configuration

```bash
# Login to Azure
az login

# Set subscription
az account set --subscription YOUR_SUBSCRIPTION_ID

# Configure environment
cp config/environments/development.env.template config/environments/development.env
# Edit development.env with your Azure resource details
```

### 3. Environment Variables

Set these key environment variables:
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_SEARCH_ENDPOINT` 
- `AZURE_COSMOS_ENDPOINT`
- `AZURE_STORAGE_ACCOUNT`

## TODO-Driven Development Workflow

### 1. Current Implementation State

**⚠️ All code is in TODO-only state with Enterprise-Grade Data Types:**
- **All method implementations replaced** with `pass` and comprehensive TODOs
- **All enum values cleaned** to TODO guidance  
- **Centralized data type system implemented** - 7 model files in `models/` directory (including enums)
- **100% type-safe function signatures** - all `Dict[str, Any]` return types replaced
- **43 files systematically updated** with centralized model imports
- **Zero local BaseModel violations** - all moved to centralized models
- **Pre-commit hooks enhanced** with data type violation detection

### 2. Architecture Principles (Design Goals)

The architecture is designed around these principles:
- **No hardcoded values** - All business logic values must be learned or configurable (enforced by pre-commit hooks)
- **Data-driven configuration** - Configurations generated from corpus analysis (TODO-guided)
- **Communication-driven** - Agents negotiate requirements, never assume (TODO-guided)
- **Performance-feedback driven** - All configurations evolve based on performance (TODO-guided)

### 3. Implementation Approach

#### Starting Implementation (Current State)

**Example of current TODO-driven state:**

```python
# agents/your_agent/agent.py - CURRENT STATE
from pydantic_ai import Agent
# TODO: Import toolsets once implemented
# from .toolsets import YourAgentToolset
# TODO: Import dependencies once implemented  
# from .deps import YourAgentDeps

class YourAgent:
    def __init__(self):
        # TODO: Initialize PydanticAI agent with Azure OpenAI model
        # TODO: Set up toolsets for agent capabilities
        # TODO: Configure system prompt based on agent role
        # TODO: Initialize dependencies with proper injection
        pass
    
    async def process_request(self, request_data):
        # TODO: Implement request processing logic
        # TODO: Use learned configuration - NO hardcoded values
        # TODO: Apply agent-specific processing workflow
        # TODO: Return results with confidence scoring
        pass
```

#### Implementation Steps

1. **Choose starting component** (recommended: `agents/supports/config_provider.py`)
2. **Review TODOs** in the chosen file (now includes enterprise features)
3. **Implement incrementally** following TODO guidance (basic → enterprise)
4. **Test with pre-commit hooks** to ensure zero-hardcoded-values
5. **Move to dependent components**

#### Enterprise Features Implementation Path

**Phase 1: Core Infrastructure**
- `agents/supports/config_provider.py` - Anti-hardcoding enforcement & memory management
- `azure_services/openai_client.py` - Consolidated Azure services orchestration
- `agents/supports/perf_monitor.py` - Enterprise monitoring infrastructure

**Phase 2: Advanced Analytics**
- `agents/auto_domain/pattern_learner.py` - Sophisticated pattern discovery & statistical analysis
- `agents/graph_flows/state_persist.py` - Advanced workflow orchestration with audit trails
- `azure_services/ml_client.py` - Production GNN model management

**Phase 3: Integration & Optimization**  
- Cross-component integration of enterprise features
- Performance optimization with sub-3-second response targets
- Comprehensive monitoring and analytics dashboards

#### Enterprise TODO Categories

**🔒 Anti-Hardcoding Enforcement**
```python
# TODO: Initialize ConfigEnforcement validation system
# TODO: Set up violation detection and reporting mechanisms
# TODO: Configure dynamic configuration learning with cache TTL
```

**💾 Memory & Cache Management**
```python
# TODO: Implement UnifiedMemoryManager with LRU eviction and bounds checking
# TODO: Add QueryPatternIndex for O(1) domain pattern matching
# TODO: Create performance metrics collection for sub-3-second optimization
```

**☁️ Azure Services Orchestration**
```python
# TODO: Implement ConsolidatedAzureServices with parallel initialization
# TODO: Add health monitoring and service status tracking
# TODO: Create Azure cost tracking and estimation system
```

#### Agent Communication (TODO-Guided Implementation)

**Current State**: Communication system is TODO-driven

```python
# CURRENT STATE - TODO guidance for implementation
from agents.supports.graph_comm import GraphComm

class YourAgent:
    async def request_configuration(self, requirements):
        # TODO: Initialize GraphComm for agent communication
        # TODO: Request configuration from config provider
        # TODO: Handle communication timeouts and retries
        # TODO: Validate received configuration structure
        # TODO: Return validated configuration for use
        pass
```

### 4. Configuration Management (TODO-Guided)

**Current State**: ConfigProvider is TODO-driven, enforcement via pre-commit hooks

```python
# ❌ WRONG - Hardcoded values (BLOCKED by pre-commit hooks)
similarity_threshold = 0.7  # Pre-commit hook will block this
hop_count = 2               # Pre-commit hook will block this

# ✅ CORRECT - Data-driven configuration (TODO-guided implementation)
from agents.supports.config_provider import ConfigProvider

class YourService:
    async def get_configuration(self, domain, query_type):
        # TODO: Initialize ConfigProvider with zero hardcoded values
        # TODO: Request domain-specific configuration
        # TODO: Handle configuration unavailable gracefully
        # TODO: Return learned configuration without fallbacks
        pass
```

### 4. Prompt Flow Development

#### Creating Templates

Templates use Jinja2 with domain context:

```jinja2
# prompt_flows/templates/your_template.jinja2
You are analyzing {{domain}} content with {{technical_density}} technical density.

{% for pattern in domain_patterns %}
- Focus on {{pattern.type}}: {{pattern.description}}
{% endfor %}

Content: {{content}}
```

#### Workflow Definitions

Define workflows in YAML:

```yaml
# prompt_flows/defs/your_workflow.yaml
workflow_id: "your_workflow"
description: "Your workflow description"
stages:
  - name: "analysis"
    type: "llm"
    template: "your_template.jinja2"
    inputs: [domain, content]
    outputs: [analysis_result]
```

### 5. Testing Guidelines

#### Unit Tests

```python
# tests/unit/test_your_feature.py
import pytest
from agents.your_agent.agent import YourAgent

@pytest.mark.asyncio
async def test_your_agent_functionality():
    agent = YourAgent()
    result = await agent.process_request(test_data)
    assert result.confidence > 0.8
```

#### Integration Tests

```python
# tests/integration/test_your_integration.py
@pytest.mark.asyncio
async def test_end_to_end_workflow():
    # Test complete workflow from domain analysis to search
    pass
```

### 6. Performance Optimization

#### Monitoring Performance

```python
from agents.supports.perf_monitor import PerfMonitor

perf_monitor = PerfMonitor()
execution_id = await perf_monitor.start_execution_tracking(config)
# ... perform operations
await perf_monitor.end_execution_tracking(execution_id, metrics)
```

#### Learning from Feedback

```python
from agents.supports.learn_feedback import LearnFeedback

feedback = LearnFeedback()
await feedback.collect_performance_metrics(execution_id, metrics)
suggestions = await feedback.generate_optimization_suggestions(analysis)
```

## Code Quality Standards

### 1. Anti-Hardcoding Enforcement

Pre-commit hooks automatically check for hardcoded values:

```bash
# Install pre-commit hook
cp scripts/hooks/pre-commit-anti-hardcoding.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

### 2. Centralized Data Types

**🏆 Enterprise-Grade Data Type System Implemented**

The project features a complete centralized data type system in the `models/` directory:

```python
# ✅ CORRECT - Use centralized models
from models.domain import DomainConfig, CorpusAnalysis
from models.knowledge import KnowledgeExtraction, EntityResult
from models.search import SearchResults, SearchResponse
from models.azure import AzureServiceResponse, EmbeddingResult
from models.workflow import WorkflowContext, TemplateConfig
from models.validation import ValidationResult, ConfigValidation
from models.enums import FlowType, FlowStatus

# Function signatures use structured return types
async def analyze_corpus(domain_path: str) -> CorpusAnalysis:
    # TODO: Implement domain analysis
    # LLMs generate values that fit CorpusAnalysis structure
    pass

async def extract_knowledge(text: str, config: Dict[str, Any]) -> KnowledgeExtraction:
    # TODO: Implement knowledge extraction
    # Parameters remain flexible, return types are structured
    pass
```

**Key Benefits**:
- **100% type-safe function signatures** - no `Dict[str, Any]` return types
- **Full IDE support** - autocomplete and validation
- **Self-documenting code** - clear data contracts
- **LLM integration ready** - structured models for generated content
- **Zero violations enforced** - pre-commit hook detection

### 3. Type Safety

All models are TODO-defined and ready for implementation:

```python
# models/domain.py example
class DomainConfig(BaseModel):
    # TODO: Define similarity_threshold float field (0.0-1.0)
    # TODO: Define max_results int field (>0) 
    # TODO: Define entity_confidence_threshold float field (0.0-1.0)
    pass
```

### 4. Error Handling

Implement comprehensive error handling:

```python
try:
    result = await agent.process(data)
except ConfigurationNotAvailableError:
    # Trigger configuration generation
    await trigger_config_generation(domain)
    result = await agent.process(data)
```

## Debugging and Troubleshooting

### 1. Common Issues

#### Configuration Not Found
```
ConfigurationNotAvailableError: No learned configuration for domain_query_type
```
**Solution**: Run domain analysis workflow first

#### Azure Authentication
```
DefaultAzureCredential failed to retrieve a token
```
**Solution**: Run `az login` or check managed identity setup

### 2. Logging

Use structured logging:

```python
import logging
logger = logging.getLogger(__name__)

logger.info("Processing started", extra={
    "domain": domain,
    "query_type": query_type,
    "execution_id": execution_id
})
```

### 3. Performance Debugging

Monitor execution with performance tracking:

```python
# Check performance insights
insights = await perf_monitor.get_performance_insights(config_hash)
print(f"Average response time: {insights.avg_response_time}")
```

## Deployment

### 1. Local Development

```bash
# Start development server
python -m uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Azure Deployment

```bash
# Deploy infrastructure
cd infra
az deployment group create --resource-group rg-your-project --template-file main.bicep

# Deploy application
# (Application deployment instructions)
```

## Best Practices

1. **Always use async/await** for Azure operations
2. **Implement graceful degradation** when services unavailable
3. **Use dependency injection** for testability
4. **Follow the dual-graph communication pattern** 
5. **Capture performance metrics** for continuous learning
6. **Write comprehensive tests** for all components
7. **Document architectural decisions** and patterns

## Contributing

1. Create feature branch from main
2. Implement following architecture patterns
3. Add comprehensive tests
4. Ensure no hardcoded values (pre-commit hook enforces this)
5. Update documentation
6. Submit pull request

## Resources

- [Architecture Design](../architecture/AZURE_INTELLIGENT_RAG_DESIGN.md)
- [Dual Graph Design](../architecture/DUAL_GRAPH_DESIGN.md) 
- [API Documentation](../api/API_ENDPOINTS.md)
- [Getting Started Guide](GETTING_STARTED.md)