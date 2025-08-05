# Universal RAG Azure

**🚧 TODO-Driven Development Stage**

A clean implementation of the dual-graph workflow architecture that demonstrates intelligent, data-driven configuration without any hardcoded fallbacks. **Currently in TODO-driven development phase** - all implementation has been systematically cleaned to provide comprehensive development guidance through TODOs.

## Table of Contents

- [Current Status: TODO-Driven Development](#current-status-todo-driven-development)
- [🚀 Quick Start](#-quick-start)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Current Development State](#current-development-state)
- [📁 Project Structure](#-project-structure)
- [🔄 Workflow Diagram](#-workflow-diagram)
- [Architecture Overview](#architecture-overview)
- [Current Development State](#current-development-state-1)
  - [✅ Completed Cleanup](#-completed-cleanup)
  - [🔄 Ready for Implementation](#-ready-for-implementation)
- [Key Features (Architecture Design)](#key-features-architecture-design)
- [Development Approach](#development-approach)
- [📚 Documentation Reference](#-documentation-reference)
  - [📋 Core Documentation](#-core-documentation)
  - [📖 Documentation Hub](#-documentation-hub)
  - [🚀 Getting Started & Development](#-getting-started--development)
  - [🏗️ Architecture & Design](#️-architecture--design)
  - [🌐 API Reference](#-api-reference)
  - [📋 Quick Navigation by Role](#-quick-navigation-by-role)
  - [🔄 Documentation Status](#-documentation-status)
- [Next Steps for Developers](#next-steps-for-developers)

## Current Status: TODO-Driven Development

**⚠️ Implementation Status: All code cleaned to TODO-only state with Enterprise-Grade Data Types**

This codebase is currently in a **TODO-driven development phase** where:
- ✅ **All hardcoded values removed** - zero-hardcoded-values principle enforced
- ✅ **All enum implementations cleaned** to comprehensive TODOs
- ✅ **All method implementations replaced** with detailed TODO guidance
- ✅ **Centralized data type system implemented** - 7 model files with 100% type safety (including enums)
- ✅ **43 files updated** with centralized model imports
- ✅ **Zero function return type violations** - all `Dict[str, Any]` eliminated
- ✅ **Pre-commit hooks enhanced** with data type violation detection
- ✅ **Enterprise-grade type safety achieved** while maintaining TODO-driven approach

## 🚀 Quick Start

### Prerequisites

- **Python 3.9+**
- **Azure subscription** (for service integration)
- **Git** with pre-commit hooks support
- **Azure CLI** (for deployment)

### Installation

```bash
# Clone the repository
git clone <repository-url>
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

### Current Development State

**⚠️ Important**: This project is in **TODO-driven development phase**

```bash
# Verify TODO state
find . -name "*.py" -exec grep -l "TODO" {} \; | wc -l
# Should show numerous files with TODO guidance

# API will NOT start until TODOs are implemented
# python -m api.main  # Will fail - implementation needed

# Start with configuration components
cd agents/supports/
cat config_provider.py  # Review comprehensive TODOs
```

## 📁 Project Structure

```
universal-rag-azure/
├── 📄 README.md                     # Main project documentation
├── 📄 CLAUDE.md                     # Project status and accomplishments
├── 📦 requirements.txt              # Python dependencies
├── ⚙️  pyproject.toml               # Project configuration
│
├── 🤖 agents/                       # Multi-agent system (TODO-driven)
│   ├── 🏢 auto_domain/             # Domain configuration generation
│   │   ├── agent.py                # Main domain analysis agent
│   │   ├── corpus_analyzer.py      # Document corpus analysis
│   │   ├── pattern_learner.py      # Domain pattern learning
│   │   ├── config_builder.py       # Configuration generation
│   │   ├── deps.py                 # Dependencies injection
│   │   └── tools.py                # Agent toolsets
│   │
│   ├── 🧠 gen_knowledge/           # Knowledge extraction workflows
│   │   ├── agent.py                # Main knowledge agent
│   │   ├── extractor.py            # Entity/relation extraction
│   │   ├── validator.py            # Knowledge validation
│   │   ├── deps.py                 # Dependencies injection
│   │   └── tools.py                # Agent toolsets
│   │
│   ├── 🔍 uni_search/              # Universal tri-modal search
│   │   ├── agent.py                # Main search agent
│   │   ├── orchestrator.py         # Search orchestration
│   │   ├── deps.py                 # Dependencies injection
│   │   └── tools.py                # Agent toolsets
│   │
│   ├── 🛠️ supports/                # Infrastructure & communication
│   │   ├── config_provider.py      # Intelligent configuration
│   │   ├── config_nego.py          # Configuration negotiation
│   │   ├── learn_feedback.py       # Performance learning
│   │   ├── perf_monitor.py         # Performance monitoring
│   │   ├── error_handler.py        # Error handling
│   │   └── graph_comm.py           # Graph communication
│   │
│   └── 🔄 graph_flows/             # Dual-graph orchestration
│       ├── domain_flow.py          # Domain workflow
│       ├── search_flow.py          # Search workflow
│       └── orchestrator.py         # Flow orchestration
│
├── 🌐 api/                          # FastAPI application (TODO-driven)
│   ├── main.py                     # Main FastAPI app
│   ├── endpoints/                  # API endpoints
│   │   └── search.py              # Search endpoints
│   └── __init__.py                 # API package
│
├── 📝 prompt_flows/                # YAML-driven workflows (TODO-driven)
│   ├── flow_mgr.py                 # Workflow manager
│   ├── template_mgr.py             # Template management
│   ├── prompt_composer.py          # Dynamic prompt composition
│   ├── templates/                  # Jinja2 templates
│   └── defs/                       # Workflow definitions (YAML)
│
├── ☁️ azure_services/              # Azure integrations (TODO-driven)
│   ├── openai_client.py           # Azure OpenAI client
│   ├── search_client.py           # Cognitive Search client
│   ├── cosmos_client.py            # Cosmos DB client
│   ├── ml_client.py                # Azure ML client
│   └── storage_client.py           # Blob Storage client
│
├── ⚙️ config/                       # Configuration management
│   ├── settings.py                 # Application settings
│   └── environments/               # Environment configs
│
├── 🔧 scripts/                      # Utility scripts
│   └── hooks/                      # Git hooks
│       └── pre-commit-anti-hardcoding.sh  # Zero-hardcoding enforcement
│
└── 📚 docs/                         # Documentation
    ├── README.md                   # Documentation hub
    ├── guides/                     # User guides
    │   ├── GETTING_STARTED.md      # Setup guide
    │   └── DEVELOPMENT_GUIDE.md    # Development workflow
    ├── architecture/               # Architecture docs
    │   ├── AZURE_INTELLIGENT_RAG_DESIGN.md    # Main architecture
    │   ├── DUAL_GRAPH_DESIGN.md               # Workflow design
    │   └── MIGRATION_ROADMAP.md               # Implementation strategy
    └── api/                        # API documentation
        └── API_ENDPOINTS.md        # Endpoint specifications
```

## 🔄 Workflow Diagram

### Enterprise Dual-Graph Architecture Flow

```mermaid
flowchart TD
    %% User Interaction
    User["👤 User"] --> API["🌐 FastAPI Application<br/>Enterprise Monitoring"]
    
    %% API Layer with Enterprise Features
    API --> SearchEndpoint["🔍 Search Endpoint<br/>Real-time Analytics"]
    API --> ConfigEndpoint["⚙️ Config Endpoint<br/>Anti-hardcoding Enforcement"]
    API --> DomainEndpoint["🏢 Domain Endpoint<br/>Pattern Discovery"]
    API --> EnterpriseEndpoint["🏢 Enterprise Health<br/>Comprehensive Monitoring"]
    
    %% Domain Configuration Graph (Graph 1) - Enhanced
    SearchEndpoint --> |"❓ Need Config"| AutoDomain["🏢 Auto Domain Agent<br/>Statistical Analytics"]
    AutoDomain --> CorpusAnalyzer["📊 Corpus Analyzer<br/>TF-IDF + Clustering"]
    AutoDomain --> PatternLearner["🧠 Pattern Learner<br/>Mathematical Foundation"]
    AutoDomain --> ConfigBuilder["⚙️ Config Builder<br/>Zero Hardcoded Values"]
    
    CorpusAnalyzer --> AzureServices["☁️ Consolidated Azure Services<br/>Parallel Initialization"]
    PatternLearner --> AzureServices
    ConfigBuilder --> ConfigProvider["🛠️ Config Provider<br/>Memory Management + Cache"]
    
    %% Enterprise Support Layer
    ConfigProvider --> ConfigEnforcement["🔒 Anti-hardcoding<br/>Violation Detection"]
    ConfigProvider --> MemoryManager["💾 Unified Memory<br/>LRU + O(1) Lookup"]
    
    %% Search Execution Graph (Graph 2) - Enhanced
    ConfigProvider --> |"✅ Config Ready"| UniSearch["🔍 Universal Search Agent<br/>Cross-modal Agreement"]
    UniSearch --> SearchOrchestrator["🎭 Search Orchestrator<br/>Tri-modal Synthesis"]
    
    SearchOrchestrator --> VectorSearch["🔗 Vector Search<br/>1536D Embeddings"]
    SearchOrchestrator --> GraphSearch["🕸️ Graph Search<br/>Multi-hop Reasoning"]
    SearchOrchestrator --> GNNSearch["🧠 GNN Search<br/>PyTorch Geometric"]
    
    VectorSearch --> AzureServices
    GraphSearch --> AzureServices
    GNNSearch --> MLClient["🤖 Azure ML Client<br/>GNN Model Management"]
    
    %% Knowledge Generation (Supporting Flow) - Enhanced
    DomainEndpoint --> GenKnowledge["🧠 Gen Knowledge Agent<br/>Evidence Tracking"]
    GenKnowledge --> Extractor["🔍 Extractor<br/>Multi-method Extraction"]
    GenKnowledge --> Validator["✅ Validator<br/>Quality Assessment"]
    GenKnowledge --> MLClient
    
    %% Advanced Workflow Orchestration
    ConfigProvider <--> GraphComm["🔄 Graph Communication<br/>Bidirectional Messaging"]
    UniSearch <--> GraphComm
    GenKnowledge <--> GraphComm
    GraphComm --> WorkflowOrchestrator["🔄 Workflow Orchestrator<br/>State Persistence + Recovery"]
    
    %% Enterprise Performance & Learning
    UniSearch --> PerfMonitor["📊 Performance Monitor<br/>OpenTelemetry Integration"]
    PerfMonitor --> LearnFeedback["📈 Learn Feedback<br/>Optimization Engine"]
    LearnFeedback --> ConfigProvider
    PerfMonitor --> EnterpriseMonitoring["📈 Enterprise Analytics<br/>Evidence Chains + Dashboards"]
    
    %% Azure Services Detail - Enhanced
    AzureServices --> OpenAI["🤖 Azure OpenAI<br/>Cost Tracking"]
    AzureServices --> CognitiveSearch["🔍 Cognitive Search<br/>Health Monitoring"]
    AzureServices --> CosmosDB["🗄️ Cosmos DB<br/>Graph Operations"]
    AzureServices --> BlobStorage["📦 Blob Storage<br/>Document Management"]
    MLClient --> MachineLearning["⚙️ Azure ML<br/>GNN Training + Inference"]
    
    %% Response Flow with Analytics
    SearchOrchestrator --> |"📊 Results + Metrics"| SearchEndpoint
    SearchEndpoint --> |"📋 Response + Analytics"| User
    
    %% Enterprise Features Integration
    EnterpriseEndpoint --> EnterpriseMonitoring
    EnterpriseMonitoring --> ConfigEnforcement
    EnterpriseMonitoring --> MemoryManager
    EnterpriseMonitoring --> WorkflowOrchestrator
    
    %% Styling
    classDef userClass fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef apiClass fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef agentClass fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    classDef azureClass fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef supportClass fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    classDef enterpriseClass fill:#e8eaf6,stroke:#3f51b5,stroke-width:3px
    
    class User userClass
    class API,SearchEndpoint,ConfigEndpoint,DomainEndpoint,EnterpriseEndpoint apiClass
    class AutoDomain,UniSearch,GenKnowledge agentClass
    class AzureServices,OpenAI,CognitiveSearch,CosmosDB,BlobStorage,MachineLearning,MLClient azureClass
    class ConfigProvider,GraphComm,PerfMonitor,LearnFeedback supportClass
    class ConfigEnforcement,MemoryManager,WorkflowOrchestrator,EnterpriseMonitoring enterpriseClass
```

### Workflow Execution Flow

The enhanced dual-graph workflow with enterprise features and intelligent communication:

```mermaid
sequenceDiagram
    participant AD as AutoDomainAgent
    participant FM as FlowMgr
    participant TM as TemplateMgr
    participant GC as GraphComm
    participant CN as ConfigNego
    participant US as UniSearchAgent
    participant PM as PerfMonitor
    participant LF as LearnFeedback
    participant AB as Azure Backend
    participant EM as EnterpriseMonitoring

    Note over AD,US: 🎯 ENHANCED Phase 1: Intelligent Config Generation with Prompt Flows
    AD->>FM: "Execute domain analysis workflow"
    FM->>TM: Load domain_analyze.jinja2 template
    TM->>FM: Rendered domain analysis prompt
    FM->>AD: Execute corpus analysis with context-aware prompts
    AD->>AD: Statistical + LLM hybrid analysis via prompt flows
    AD->>GC: "Domain analysis complete, ready to provide configs"
    GC->>AB: Persist domain analysis results
    AD->>EM: Report anti-hardcoding compliance + performance metrics

    Note over CN,US: 🤝 ENHANCED Phase 2: Negotiated Config Transfer
    US->>CN: "Need config for query_type=technical, domain=programming"
    CN->>GC: Request specific configuration requirements
    GC->>AD: "Provide: similarity_threshold, tri_modal_weights, hop_count"
    AD->>FM: Execute config_gen.jinja2 workflow
    FM->>TM: Load configuration generation template
    TM->>AD: Context-aware config generation prompts
    AD->>CN: "Delivering: similarity=0.82, weights={v:0.4,g:0.35,gnn:0.25}"
    CN->>US: Validated configuration with source tracking
    CN->>EM: Log configuration negotiation + compliance validation

    Note over US,PM: 🚀 ENHANCED Phase 3: Monitored Search Execution
    US->>PM: Start execution tracking with config_hash
    US->>FM: Execute search optimization prompts if needed
    US->>US: Execute tri-modal search with provided config
    PM->>PM: Record: response_time, relevance_score, satisfaction
    PM->>LF: Performance metrics with config correlation
    PM->>EM: Real-time performance analytics + evidence chains

    Note over LF,AD: 🎓 ENHANCED Phase 4: Adaptive Learning Loop
    LF->>LF: Analyze config effectiveness across queries
    LF->>GC: "Optimization: reduce similarity to 0.78 for speed"
    GC->>AD: Configuration adjustment recommendations
    AD->>FM: Update prompt templates based on performance
    AD->>AD: Update learned patterns based on performance
    AD->>AB: Persist evolved domain intelligence
    LF->>EM: Learning optimization insights + quality validation

    Note over EM: 🏢 ENHANCED Phase 5: Enterprise Monitoring & Analytics
    EM->>EM: Aggregate cross-modal agreement analysis
    EM->>EM: Generate evidence chains for audit compliance
    EM->>EM: Monitor memory management + cache performance
    EM->>EM: Track Azure costs + service health status
    EM->>AB: Persist enterprise analytics + compliance reports
```

### Intelligent Communication Architecture

The sophisticated bidirectional communication system between dual graphs:

```mermaid
sequenceDiagram
    participant CE as Config-Extraction Graph
    participant GC as Graph Communicator
    participant CN as Config Negotiator
    participant LF as Learning Feedback
    participant SG as Search Graph
    participant PM as Performance Monitor
    participant EM as Enterprise Monitor

    Note over CE,SG: 🎯 PHASE 1: Intelligent Handshake
    CE->>GC: "I've analyzed domain X, ready to provide config"
    GC->>CN: Initiate config negotiation
    CN->>SG: "Config-Extraction ready, what do you need?"
    SG->>CN: "Need: similarity_threshold, tri_modal_weights, hop_count for query_type=technical"
    CN->>CE: Negotiate specific config requirements
    CE->>CN: "Providing: similarity=0.82 (learned), weights={vector:0.4, graph:0.35, gnn:0.25}, hops=3"
    CN->>SG: Deliver negotiated configuration
    CN->>EM: Log negotiation process + compliance validation

    Note over SG,CE: 🔄 PHASE 2: Real-Time Performance Feedback
    SG->>PM: Execute search with provided config
    PM->>PM: Monitor: response_time=1.2s, relevance_score=0.87, user_satisfaction=0.91
    PM->>LF: Performance metrics
    LF->>GC: "Config performed well, but response_time slow for similarity=0.82"
    GC->>CE: "Adjust similarity_threshold down to 0.78 for better speed/relevance balance"
    CE->>CE: Update learned patterns based on feedback
    PM->>EM: Real-time performance analytics + evidence collection

    Note over CE,SG: 🚀 PHASE 3: Adaptive Optimization
    SG->>CN: "Next query: query_type=creative, domain=programming"
    CN->>CE: "Request: Config for creative queries in programming domain"
    CE->>CN: "Providing: similarity=0.75 (adapted), weights={vector:0.3, graph:0.5, gnn:0.2}, hops=2"
    CN->>SG: Deliver domain+query-adapted config
    CN->>EM: Track configuration adaptation + optimization metrics

    Note over PM,EM: 🎓 PHASE 4: Continuous Learning Loop + Enterprise Analytics
    PM->>LF: Aggregate performance across query types
    LF->>CE: "Creative queries perform better with graph_weight=0.5, technical queries with vector_weight=0.4"
    CE->>CE: Update domain-specific patterns
    EM->>EM: Cross-modal agreement analysis + confidence scoring
    EM->>EM: Evidence chain tracking for audit compliance
    EM->>EM: Memory management optimization + cache performance
    EM->>EM: Azure cost tracking + service health monitoring
    EM->>GC: Enterprise insights + optimization recommendations
```

### TODO-Driven Implementation Flow

```mermaid
flowchart LR
    %% Current State
    Start[🚧 Current State<br/>TODO-Only Code] --> Choose[🎯 Choose Component]
    
    %% Implementation Path
    Choose --> |"Recommended"| ConfigProvider[🛠️ Config Provider<br/>agents/supports/]
    Choose --> |"Alternative"| ErrorHandler[❌ Error Handler<br/>agents/supports/]
    
    %% Implementation Steps
    ConfigProvider --> ReviewTODOs[📖 Review TODOs]
    ReviewTODOs --> Implement[💻 Implement Methods]
    Implement --> Test[🧪 Test Pre-commit Hooks]
    Test --> |"Pass"| NextComponent[➡️ Next Component]
    Test --> |"Fail"| FixHardcoding[🔧 Fix Hardcoded Values]
    FixHardcoding --> Test
    
    %% Component Flow
    NextComponent --> AzureServices[☁️ Azure Services]
    AzureServices --> AutoDomain[🏢 Auto Domain]
    AutoDomain --> API[🌐 API Endpoints]
    API --> UniSearch[🔍 Universal Search]
    UniSearch --> PromptFlows[📝 Prompt Flows]
    PromptFlows --> Complete[✅ Implementation Complete]
    
    %% Styling
    classDef todoClass fill:#ffecb3,stroke:#f57f17,stroke-width:2px
    classDef implementClass fill:#c8e6c9,stroke:#388e3c,stroke-width:2px
    classDef testClass fill:#e1bee7,stroke:#7b1fa2,stroke-width:2px
    classDef completeClass fill:#a5d6a7,stroke:#2e7d32,stroke-width:3px
    
    class Start,ReviewTODOs todoClass
    class Choose,Implement,NextComponent implementClass
    class Test,FixHardcoding testClass
    class Complete completeClass
```

## Architecture Overview

This system implements a dual-graph workflow with **comprehensive enterprise-grade TODO guidance**:

- **agents/auto_domain/** - Domain configuration generation with sophisticated analytics (TODO-driven)
  - Advanced statistical analysis with TF-IDF, entropy scoring, and clustering
  - Data-driven pattern engine with mathematical foundation
  - Domain signature caching with confidence scoring
  
- **agents/gen_knowledge/** - Knowledge extraction workflows (TODO-driven)
  - Multi-modal knowledge extraction with validation pipelines
  - Enterprise evidence tracking and audit capabilities
  
- **agents/uni_search/** - Universal tri-modal search (TODO-driven)
  - Vector + Graph + GNN search orchestration
  - Cross-modal agreement analysis for result synthesis
  
- **agents/supports/** - Enterprise infrastructure & communication (TODO-driven)
  - Advanced anti-hardcoding enforcement with violation detection
  - UnifiedMemoryManager with LRU eviction and bounds checking
  - QueryPatternIndex for O(1) domain pattern matching
  - Comprehensive monitoring with OpenTelemetry integration
  
- **agents/graph_flows/** - Advanced workflow orchestration (TODO-driven)
  - Graph-based workflow system with node dependencies
  - Workflow state persistence and recovery mechanisms
  - Cross-workflow integration bridge with audit trails
  
- **api/** - FastAPI endpoints with enterprise monitoring (TODO-driven)
  - Performance tracking and health monitoring endpoints
  - Real-time analytics and cost tracking integration
  
- **prompt_flows/** - YAML-driven prompt workflows (TODO-driven)
  - Advanced template management with inheritance
  - Dynamic prompt composition with performance optimization
  
- **azure_services/** - Consolidated Azure service orchestration (TODO-driven)
  - Parallel service initialization with health monitoring
  - Azure cost tracking and estimation system
  - Universal GNN architecture with PyTorch Geometric
  - Production-ready model lifecycle management

## Current Development State

### ✅ Completed Cleanup
- All agent modules systematically cleaned
- All API endpoints converted to TODOs
- All prompt flow components cleaned
- All Azure service clients cleaned
- Pre-commit hooks enhanced with cleanup patterns

### 🔄 Ready for Implementation
- Comprehensive TODOs provide implementation guidance
- Zero hardcoded values - all configuration must be learned/provided
- Pydantic models ready for field definitions
- Agent classes ready for method implementations
- FastAPI endpoints ready for route implementations

## Key Features (Architecture Design)

- ✅ Zero hardcoded values (enforced by pre-commit hooks)
- ✅ TODO-driven development with comprehensive guidance
- ✅ Intelligent configuration generation architecture
- ✅ Dual-graph workflow architecture design
- ✅ Anti-hardcoding enforcement system
- ✅ PydanticAI multi-agent system design
- ✅ Azure-native service integration architecture

## Development Approach

This project follows **TODO-driven development**:
1. Each file contains comprehensive TODOs explaining what needs to be implemented
2. No hardcoded values allowed - all configuration must be dynamic
3. Pre-commit hooks prevent hardcoded value introduction
4. Implementation should be done incrementally, following TODOs

## 📚 Documentation Reference

### 📋 Core Documentation
- **[`README.md`](README.md)** - This file: Main project overview and current status
- **[`CLAUDE.md`](CLAUDE.md)** - Claude Code project status and technical accomplishments

### 📖 Documentation Hub
- **[`docs/README.md`](docs/README.md)** - Documentation overview and navigation hub

### 🚀 Getting Started & Development
- **[`docs/guides/TODO_DRIVEN_IMPLEMENTATION_GUIDE.md`](docs/guides/TODO_DRIVEN_IMPLEMENTATION_GUIDE.md)** - **🎯 OFFICIAL IMPLEMENTATION METHODOLOGY** - TODO + Basic Code pattern with complete 8-phase roadmap
- **[`docs/guides/GETTING_STARTED.md`](docs/guides/GETTING_STARTED.md)** - TODO-driven development setup and approach
- **[`docs/guides/DEVELOPMENT_GUIDE.md`](docs/guides/DEVELOPMENT_GUIDE.md)** - Comprehensive implementation guidance and workflows

### 🏗️ Architecture & Design
- **[`docs/architecture/AZURE_INTELLIGENT_RAG_DESIGN.md`](docs/architecture/AZURE_INTELLIGENT_RAG_DESIGN.md)** - Main architecture design and system overview
- **[`docs/architecture/DUAL_GRAPH_DESIGN.md`](docs/architecture/DUAL_GRAPH_DESIGN.md)** - Dual-graph workflow architecture specifications
- **[`docs/architecture/CONFIG_GENERATION_ARCHITECTURE.md`](docs/architecture/CONFIG_GENERATION_ARCHITECTURE.md)** - Automatic configuration generation system (zero-hardcoded-values)
- **[`docs/architecture/MIGRATION_ROADMAP.md`](docs/architecture/MIGRATION_ROADMAP.md)** - Migration strategy and implementation roadmap

### 🌐 API Reference
- **[`docs/api/API_ENDPOINTS.md`](docs/api/API_ENDPOINTS.md)** - Complete API specification and endpoint documentation (TODO state)

### 📋 Quick Navigation by Role

#### 👨‍💻 **New Developers**
1. **START HERE**: [`docs/guides/TODO_DRIVEN_IMPLEMENTATION_GUIDE.md`](docs/guides/TODO_DRIVEN_IMPLEMENTATION_GUIDE.md) - **OFFICIAL IMPLEMENTATION METHODOLOGY**
2. Project overview: [`README.md`](README.md) (Current file)
3. Setup guide: [`docs/guides/GETTING_STARTED.md`](docs/guides/GETTING_STARTED.md)
4. Development workflow: [`docs/guides/DEVELOPMENT_GUIDE.md`](docs/guides/DEVELOPMENT_GUIDE.md)

#### 🏗️ **System Architects**
1. Architecture overview: [`docs/architecture/AZURE_INTELLIGENT_RAG_DESIGN.md`](docs/architecture/AZURE_INTELLIGENT_RAG_DESIGN.md)
2. Workflow design: [`docs/architecture/DUAL_GRAPH_DESIGN.md`](docs/architecture/DUAL_GRAPH_DESIGN.md)
3. Implementation strategy: [`docs/architecture/MIGRATION_ROADMAP.md`](docs/architecture/MIGRATION_ROADMAP.md)

#### 🌐 **API Developers**
1. API specifications: [`docs/api/API_ENDPOINTS.md`](docs/api/API_ENDPOINTS.md)
2. Development guide: [`docs/guides/DEVELOPMENT_GUIDE.md`](docs/guides/DEVELOPMENT_GUIDE.md)
3. Architecture context: [`docs/architecture/AZURE_INTELLIGENT_RAG_DESIGN.md`](docs/architecture/AZURE_INTELLIGENT_RAG_DESIGN.md)

#### 📊 **Project Managers**
1. Project status: [`CLAUDE.md`](CLAUDE.md)
2. Implementation roadmap: [`docs/architecture/MIGRATION_ROADMAP.md`](docs/architecture/MIGRATION_ROADMAP.md)
3. Documentation hub: [`docs/README.md`](docs/README.md)

### 🔄 Documentation Status

| Category | Files | Status | Description |
|----------|-------|--------|-------------|
| **Core** | 2 | ✅ Complete | Main project documentation |
| **Guides** | 3 | ✅ Complete | Setup, development guidance, and **OFFICIAL IMPLEMENTATION METHODOLOGY** |
| **Architecture** | 4 | ✅ Complete | System design and strategy |
| **API** | 1 | ✅ Complete | Endpoint specifications |

**Total: 9 markdown files with comprehensive TODO-driven development guidance**

## Next Steps for Developers

### **🚀 RECOMMENDED STARTING APPROACH**

1. **Read the Official Implementation Guide**: [`docs/guides/TODO_DRIVEN_IMPLEMENTATION_GUIDE.md`](docs/guides/TODO_DRIVEN_IMPLEMENTATION_GUIDE.md)
2. **Follow the 8-Phase Roadmap**: Start with Phase 1 (Foundation Layer)
3. **Use the TODO + Basic Code Pattern**: Preserve TODOs + Add working implementation below
4. **Maintain Zero-Hardcoded-Values**: Use centralized constants and generated values
5. **Follow File Dependencies**: Implement in the specified order for smooth progress

### **Quick Start Implementation Path**
```bash
# Phase 1: Foundation (Week 1)
1. ✅ config/constants.py                     # COMPLETED
2. ✅ models/domain.py                        # COMPLETED  
3. ✅ agents/supports/config_provider.py     # COMPLETED
4. agents/supports/error_handler.py          # NEXT - Basic error handling
5. agents/supports/ai_provider.py            # Basic OpenAI client wrapper
```

The **TODO-Driven Implementation Guide** provides the complete roadmap with 44 files organized into 8 phases, ensuring systematic development while maintaining the innovative zero-hardcoded-values architecture.