# API Endpoints Documentation

## Overview

The Azure Intelligent RAG system provides RESTful API endpoints for dual-graph workflow operations, including domain analysis, knowledge extraction, and intelligent search.

## Base URL

```
http://localhost:8000  # Development
https://your-app.azurewebsites.net  # Production
```

## Authentication

The API uses Azure Active Directory authentication:

```http
Authorization: Bearer <your-jwt-token>
```

## Health Check

### GET /health

Check system health and service availability.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00Z",
  "services": {
    "azure_openai": "healthy",
    "azure_search": "healthy", 
    "azure_cosmos": "healthy",
    "azure_storage": "healthy",
    "azure_ml": "healthy"
  },
  "version": "1.0.0"
}
```

## Search Endpoints

### POST /api/search

Perform intelligent tri-modal search with automatic configuration.

**Request:**
```json
{
  "query": "What are the best practices for async programming?",
  "domain": "programming",
  "query_type": "technical",
  "max_results": 10,
  "include_explanations": true,
  "stream_progress": false
}
```

**Response:**
```json
{
  "results": [
    {
      "content": "Async programming best practices include...",
      "confidence": 0.92,
      "source": "document_id_123",
      "modality_scores": {
        "vector": 0.87,
        "graph": 0.94,
        "gnn": 0.89
      },
      "explanation": "High relevance due to exact terminology match..."
    }
  ],
  "metadata": {
    "total_results": 15,
    "execution_time": 1.24,
    "configuration_used": {
      "similarity_threshold": 0.82,
      "tri_modal_weights": {"vector": 0.4, "graph": 0.35, "gnn": 0.25},
      "hop_count": 3
    },
    "performance_prediction": {
      "confidence": 0.89,
      "expected_satisfaction": 0.91
    }
  }
}
```

### POST /api/search/stream

Streaming search with real-time progress updates.

**Request:**
```json
{
  "query": "Machine learning model deployment strategies",
  "domain": "machine_learning",
  "query_type": "analytical"
}
```

**Response:** Server-Sent Events stream
```
data: {"stage": "config_generation", "progress": 10, "message": "Analyzing domain..."}

data: {"stage": "vector_search", "progress": 40, "results": 3}

data: {"stage": "graph_search", "progress": 70, "results": 5}

data: {"stage": "gnn_inference", "progress": 90, "results": 2}

data: {"stage": "synthesis", "progress": 100, "final_results": 8}
```

### GET /api/search/domains

Get available domains and their analysis status.

**Response:**
```json
{
  "domains": [
    {
      "name": "programming",
      "display_name": "Programming & Software Development",
      "status": "analyzed",
      "document_count": 1247,
      "last_analysis": "2024-01-15T09:15:00Z",
      "quality_metrics": {
        "vocabulary_richness": 0.87,
        "technical_density": 0.92,
        "complexity_score": 0.79
      }
    },
    {
      "name": "machine_learning", 
      "display_name": "Machine Learning & AI",
      "status": "analyzing",
      "document_count": 892,
      "analysis_progress": 0.65
    }
  ]
}
```

## Configuration Endpoints

### GET /api/config/domain/{domain}

Get learned configuration for a specific domain.

**Response:**
```json
{
  "domain": "programming",
  "configurations": {
    "technical": {
      "similarity_threshold": 0.82,
      "tri_modal_weights": {"vector": 0.4, "graph": 0.35, "gnn": 0.25},
      "hop_count": 3,
      "max_results": 15,
      "confidence": 0.89,
      "last_updated": "2024-01-14T16:30:00Z"
    },
    "creative": {
      "similarity_threshold": 0.75,
      "tri_modal_weights": {"vector": 0.3, "graph": 0.5, "gnn": 0.2},
      "hop_count": 2,
      "max_results": 12,
      "confidence": 0.84,
      "last_updated": "2024-01-14T14:20:00Z"
    }
  }
}
```

### POST /api/config/optimize

Request configuration optimization for specific query patterns.

**Request:**
```json
{
  "domain": "programming",
  "query_type": "technical",
  "performance_constraints": {
    "max_response_time": 2.0,
    "min_relevance_score": 0.85
  },
  "sample_queries": [
    "async await best practices",
    "error handling patterns",
    "code review guidelines"
  ]
}
```

**Response:**
```json
{
  "optimized_config": {
    "similarity_threshold": 0.78,
    "tri_modal_weights": {"vector": 0.45, "graph": 0.35, "gnn": 0.2},
    "hop_count": 2,
    "expected_performance": {
      "response_time": 1.8,
      "relevance_score": 0.87
    }
  },
  "optimization_reasoning": "Reduced similarity threshold to improve speed while maintaining relevance...",
  "a_b_test_plan": {
    "variants": ["current", "optimized"],
    "success_metrics": ["response_time", "user_satisfaction"]
  }
}
```

## Domain Intelligence Endpoints

### POST /api/domain/analyze

Trigger domain analysis for new document collections.

**Request:**
```json
{
  "domain": "cybersecurity",
  "document_paths": [
    "data/raw/cybersecurity/security-best-practices.pdf",
    "data/raw/cybersecurity/incident-response.md"
  ],
  "analysis_config": {
    "include_statistical_analysis": true,
    "include_semantic_patterns": true,
    "quality_threshold": 0.8
  }
}
```

**Response:**
```json
{
  "analysis_id": "analysis_456789",
  "status": "started",
  "estimated_completion": "2024-01-15T11:45:00Z",
  "progress_url": "/api/domain/analyze/analysis_456789/progress"
}
```

### GET /api/domain/analyze/{analysis_id}/progress

Get domain analysis progress.

**Response:**
```json
{
  "analysis_id": "analysis_456789",
  "status": "in_progress",
  "progress": 0.67,
  "current_stage": "pattern_learning",
  "stages_completed": ["corpus_analysis"],
  "estimated_completion": "2024-01-15T11:30:00Z",
  "partial_results": {
    "vocabulary_richness": 0.84,
    "technical_density": 0.91,
    "document_count": 45
  }
}
```

## Knowledge Extraction Endpoints

### POST /api/knowledge/extract

Extract entities and relationships from documents.

**Request:**
```json
{
  "documents": [
    {
      "id": "doc_123",
      "content": "Docker containers provide process isolation...",
      "metadata": {"source": "technical_guide.md"}
    }
  ],
  "domain": "programming",
  "extraction_config": {
    "entity_threshold": 0.8,
    "relationship_threshold": 0.7,
    "include_validation": true
  }
}
```

**Response:**
```json
{
  "extraction_id": "extract_789012",
  "extracted_entities": [
    {
      "text": "Docker containers",
      "type": "technology",
      "confidence": 0.92,
      "start_pos": 0,
      "end_pos": 16,
      "context": "Docker containers provide..."
    }
  ],
  "extracted_relationships": [
    {
      "source": "Docker containers",
      "target": "process isolation", 
      "relationship_type": "provides",
      "confidence": 0.87
    }
  ],
  "knowledge_graph": {
    "nodes": 12,
    "edges": 8,
    "connectivity": 0.73
  }
}
```

## Performance Monitoring Endpoints

### GET /api/performance/insights

Get performance insights and optimization recommendations.

**Response:**
```json
{
  "overall_performance": {
    "avg_response_time": 1.34,
    "avg_relevance_score": 0.86,
    "avg_user_satisfaction": 0.89
  },
  "domain_performance": {
    "programming": {
      "query_count": 1247,
      "avg_response_time": 1.28,
      "top_performing_config": {
        "similarity_threshold": 0.82,
        "tri_modal_weights": {"vector": 0.4, "graph": 0.35, "gnn": 0.25}
      }
    }
  },
  "optimization_opportunities": [
    {
      "domain": "machine_learning",
      "query_type": "analytical", 
      "current_performance": 2.1,
      "potential_improvement": 0.3,
      "recommendation": "Reduce similarity threshold to 0.75"
    }
  ]
}
```

### POST /api/performance/feedback

Submit performance feedback for continuous learning.

**Request:**
```json
{
  "execution_id": "exec_345678",
  "user_satisfaction": 0.95,
  "relevance_ratings": [
    {"result_id": "result_1", "rating": 5},
    {"result_id": "result_2", "rating": 4}
  ],
  "response_time_rating": 5,
  "suggestions": "Results were very relevant and fast"
}
```

**Response:**
```json
{
  "feedback_recorded": true,
  "impact_on_learning": "high",
  "configuration_updates": [
    {
      "parameter": "similarity_threshold",
      "adjustment": "increased to 0.84",
      "reason": "positive satisfaction feedback"
    }
  ]
}
```

## Error Responses

All endpoints return consistent error responses:

```json
{
  "error": "ConfigurationNotFound",
  "message": "No learned configuration available for domain 'new_domain'",
  "code": "CONFIG_001",
  "suggestions": [
    "Run domain analysis first using POST /api/domain/analyze",
    "Use default configuration with 'use_defaults=true' parameter"
  ],
  "timestamp": "2024-01-15T10:30:00Z"
}
```

## Rate Limiting

API requests are rate-limited:
- **Search endpoints**: 60 requests per minute
- **Configuration endpoints**: 30 requests per minute  
- **Analysis endpoints**: 10 requests per minute

## WebSocket Support

Real-time updates available via WebSocket:

```javascript
const ws = new WebSocket('ws://localhost:8000/ws/updates');
ws.on('message', (data) => {
  const update = JSON.parse(data);
  // Handle real-time updates
});
```

## SDK Support

Official SDKs available:
- **Python**: `pip install azure-intelligent-rag-sdk`
- **TypeScript**: `npm install @azure/intelligent-rag-sdk`
- **C#**: `dotnet add package Azure.IntelligentRag.Sdk`