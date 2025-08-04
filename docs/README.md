# Universal RAG Azure Documentation

## Architecture

This system implements a dual-graph workflow architecture:

- **Domain Configuration Flow**: Automatically analyzes documents and generates intelligent configurations
- **Search Flow**: Uses those configurations for optimized search
- **Workflow Bridge**: Connects the flows without hardcoded values

## Key Components

- `agents/auto_domain/` - Automatic domain configuration generation
- `agents/gen_knowledge/` - Knowledge extraction from documents  
- `agents/uni_search/` - Universal search with tri-modal capabilities
- `agents/supports/` - Supporting infrastructure and bridges
- `agents/graph_flows/` - Dual-graph workflow orchestration

## Features

✅ Zero hardcoded values
✅ Intelligent configuration generation  
✅ Anti-hardcoding enforcement
✅ Dual-graph architecture
