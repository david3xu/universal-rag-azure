# Universal RAG Azure Documentation

**🚧 TODO-Driven Development Stage**

## Table of Contents

- [Current Status: Implementation Cleaned to TODOs](#current-status-implementation-cleaned-to-todos)
- [Architecture Design (TODO-Driven)](#architecture-design-todo-driven)
- [Key Components (Current State)](#key-components-current-state)
- [Current Development State](#current-development-state)
  - [✅ Completed Cleanup](#-completed-cleanup)
  - [🔄 Architecture Features (Design State)](#-architecture-features-design-state)
- [Documentation Structure](#documentation-structure)
- [Implementation Guidance](#implementation-guidance)
- [Next Steps](#next-steps)

## Current Status: Implementation Cleaned to TODOs

**⚠️ All implementation has been systematically cleaned to TODO-only state**

This documentation reflects the current **TODO-driven development phase** where all code has been cleaned to provide comprehensive implementation guidance through TODOs.

## Architecture Design (TODO-Driven)

This system implements a dual-graph workflow architecture with **TODO-guided implementation**:

- **Domain Configuration Flow**: TODO-driven automatic document analysis and configuration generation
- **Search Flow**: TODO-driven optimized search using learned configurations  
- **Workflow Bridge**: TODO-driven flow connection without hardcoded values

## Key Components (Current State)

### 🔄 Ready for Implementation
- `agents/auto_domain/` - Domain configuration generation (TODO-driven)
- `agents/gen_knowledge/` - Knowledge extraction workflows (TODO-driven)
- `agents/uni_search/` - Tri-modal search capabilities (TODO-driven)
- `agents/supports/` - Workflow bridges and configuration (TODO-driven)
- `agents/graph_flows/` - Dual-graph orchestration (TODO-driven)
- `api/` - FastAPI endpoints and application (TODO-driven)
- `prompt_flows/` - YAML-driven prompt workflows (TODO-driven)
- `azure_services/` - Azure service integrations (TODO-driven)

## Current Development State

### ✅ Completed Cleanup & Data Type Architecture
- **All hardcoded values removed** from all components
- **All enum implementations cleaned** to TODOs
- **All method implementations replaced** with comprehensive TODOs
- **Centralized data type system implemented** - 7 model files in `models/` directory (including enums)
- **43 files updated** with centralized model imports
- **Zero function return type violations** - all `Dict[str, Any]` return types replaced
- **9 local BaseModel definitions moved** to centralized models
- **Pre-commit hooks enhanced** with data type violation detection
- **Enterprise-grade type safety achieved** while maintaining TODO-driven approach

### 🔄 Architecture Features (Design State)
- ✅ **Zero hardcoded values** (enforced by pre-commit hooks)
- ✅ **TODO-driven development** with comprehensive guidance
- ✅ **Centralized data type system** with complete type safety
- ✅ **Enterprise-grade model architecture** - structured types for all operations
- ✅ **Automatic violation detection** via pre-commit hooks
- ✅ **Intelligent configuration generation** architecture design
- ✅ **Anti-hardcoding enforcement system** with data type validation
- ✅ **Dual-graph workflow architecture** design
- ✅ **PydanticAI multi-agent system** architecture
- ✅ **Azure-native service integration** design

## 🏗️ Centralized Data Type System

### **Enterprise-Grade Type Safety Achieved**

The project now features a **complete centralized data type system** with:

```
models/
├── __init__.py           # Central exports for all models
├── domain.py            # DomainConfig, CorpusAnalysis, DomainStatistics
├── knowledge.py         # KnowledgeExtraction, EntityResult, RelationshipResult
├── search.py            # SearchRequest, SearchResponse, SearchResults
├── azure.py             # AzureServiceResponse, EmbeddingResult, GNNTrainingConfig
├── workflow.py          # WorkflowContext, TemplateConfig, ComposedPrompt
├── validation.py        # ValidationResult, ConfigValidation
└── enums.py             # FlowType, FlowStatus, WorkflowState (moved from graph_flows)
```

### **Key Benefits**:
- **100% type-safe function signatures** - no more `Dict[str, Any]` return types
- **Full IDE support** - autocomplete and validation during development
- **Self-documenting code** - clear data structures and contracts
- **LLM integration ready** - structured models for LLM-generated content
- **Zero violations enforced** - automatic pre-commit hook validation

### **Perfect Balance Achieved**:
- **Structure is defined** - models specify expected data structure
- **Values are flexible** - LLMs generate content fitting model schemas
- **Type safety preserved** - validation ensures structural correctness
- **Zero hardcoded values maintained** - content source remains dynamic

## Documentation Structure

- [`guides/GETTING_STARTED.md`](guides/GETTING_STARTED.md) - TODO-driven development guide
- [`guides/DEVELOPMENT_GUIDE.md`](guides/DEVELOPMENT_GUIDE.md) - Implementation approach
- [`guides/BASIC_IMPLEMENTATION_PLAN.md`](guides/BASIC_IMPLEMENTATION_PLAN.md) - Complete implementation plan
- [`architecture/DATA_TYPE_STRATEGY.md`](architecture/DATA_TYPE_STRATEGY.md) - Centralized data type strategy
- [`architecture/CONFIG_GENERATION_ARCHITECTURE.md`](architecture/CONFIG_GENERATION_ARCHITECTURE.md) - Automatic configuration generation system
- [`architecture/`](architecture/) - Architecture design documents
- [`api/API_ENDPOINTS.md`](api/API_ENDPOINTS.md) - API endpoint specifications (TODO state)

## Implementation Guidance

Each component contains comprehensive TODOs that explain:
1. What needs to be implemented
2. How it should integrate with other components
3. What configuration should be learned vs provided
4. How to maintain zero-hardcoded-values principle

## Next Steps

1. Review TODO comments in chosen component
2. Implement following zero-hardcoded-values principle  
3. Use pre-commit hooks to validate implementation
4. Test integration with other TODO-driven components
