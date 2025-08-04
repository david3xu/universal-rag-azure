# Universal RAG Azure

A clean implementation of the dual-graph workflow architecture that demonstrates intelligent, data-driven configuration without any hardcoded fallbacks.


## Quick Start

```bash
# Setup
pip install -r requirements.txt

# Run
python -m api.main
```

## Architecture

This system implements a dual-graph workflow:
- **auto_domain/** - Automatically generates domain-specific configurations  
- **gen_knowledge/** - Extracts knowledge from documents
- **uni_search/** - Performs intelligent universal search
- **supports/** - Bridges workflows with intelligent configuration
- **graph_flows/** - Orchestrates the dual-graph workflows

## Key Features

- ✅ Zero hardcoded values
- ✅ Intelligent configuration generation
- ✅ Dual-graph workflow architecture
- ✅ Anti-hardcoding enforcement