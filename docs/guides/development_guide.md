# Development Guide

## Getting Started

This guide walks you through setting up and developing with the Azure Intelligent RAG dual-graph system.

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

## Development Workflow

### 1. Architecture Principles

Follow these core principles:
- **No hardcoded values** - All business logic values must be learned or configurable
- **Data-driven configuration** - Configurations generated from corpus analysis
- **Communication-driven** - Agents negotiate requirements, never assume
- **Performance-feedback driven** - All configurations evolve based on performance

### 2. Agent Development

#### Creating a New Agent

```python
# agents/your_agent/agent.py
from pydantic_ai import Agent
from .toolsets import YourAgentToolset
from .deps import YourAgentDeps

your_agent = Agent(
    get_azure_openai_model(),
    deps_type=YourAgentDeps,
    toolsets=[YourAgentToolset()],
    system_prompt="Your agent description"
)
```

#### Agent Communication

Agents communicate through the graph communication system:

```python
from agents.supports.graph_comm import GraphComm

# Request configuration
graph_comm = GraphComm()
config = await graph_comm.request_config(
    source_graph="your_agent",
    target_graph="config_provider",
    requirements=ConfigRequirements(...)
)
```

### 3. Configuration Management

Never use hardcoded values. Instead:

```python
# ❌ WRONG - Hardcoded values
similarity_threshold = 0.7
hop_count = 2

# ✅ CORRECT - Data-driven configuration
from agents.supports.config_provider import ConfigProvider

config_provider = ConfigProvider()
config = await config_provider.get_search_config(domain, query_type)
similarity_threshold = config.similarity_threshold
hop_count = config.hop_count
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

### 2. Type Safety

Use Pydantic models for all data structures:

```python
from pydantic import BaseModel, Field

class YourDataModel(BaseModel):
    field_name: str = Field(description="Field description")
    confidence: float = Field(ge=0.0, le=1.0)
```

### 3. Error Handling

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

- [Architecture Design](architecture/azure_intelligent_rag_design.md)
- [Dual Graph Design](architecture/dual_graph_design.md) 
- [API Documentation](api/endpoints.md)
- [Getting Started Guide](guides/getting_started.md)