# Getting Started

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment: `./scripts/deployment/setup-environments.sh development`

## Quick Start

1. Start the API server:
   ```bash
   python -m api.main
   ```

2. Make a search request:
   ```bash
   curl -X POST "http://localhost:8000/api/v1/search/" \
        -H "Content-Type: application/json" \
        -d '{"query": "What is machine learning?", "domain": "technical"}'
   ```

## Configuration

The system uses intelligent, data-driven configuration. No hardcoded values are allowed.
