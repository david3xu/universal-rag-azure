# Dual-Graph Design

## Table of Contents

- [Overview](#overview)
- [Components](#components)
  - [Auto Domain Agent](#auto-domain-agent)
  - [Universal Search Agent](#universal-search-agent)
  - [Knowledge Generation Agent](#knowledge-generation-agent)
  - [Workflow Bridge](#workflow-bridge)
- [Communication Flow](#communication-flow)
- [State Management](#state-management)
- [Configuration Learning](#configuration-learning)
- [Performance Optimization](#performance-optimization)

## Overview

The Universal RAG system uses a dual-graph architecture where:

1. **Config-Extraction Graph** analyzes documents and generates domain-specific configurations
2. **Search Graph** uses those configurations for intelligent search
3. **Workflow Bridge** transfers state between graphs without hardcoded fallbacks

## Components

### Auto Domain Agent
- Analyzes document corpus
- Learns domain-specific patterns
- Generates intelligent configurations

### Universal Search Agent  
- Receives intelligent configurations
- Performs tri-modal search (Vector + Graph + GNN)
- Synthesizes results using learned weights

### Workflow Bridge
- Stores configurations from Config-Extraction
- Provides configurations to Search
- Enforces no hardcoded values
