"""
Centralized Data Models

TODO-based structured Pydantic models to replace Dict[str, Any] usage throughout the codebase.
All models are in TODO stage - implementation happens when basic functionality is ready.
"""

# Domain analysis and configuration models
from .domain import DomainConfig, CorpusAnalysis, DomainStatistics, DomainDiscovery

# Knowledge extraction models
from .knowledge import KnowledgeExtraction, EntityResult, RelationshipResult, KnowledgeValidation

# Search operation models  
from .search import SearchRequest, SearchResponse, SearchResults, SearchMetrics

# Azure service integration models (includes ML models)
from .azure import (
    AzureServiceResponse, EmbeddingResult, SearchResult, ServiceHealth,
    GNNTrainingConfig, TrainingJobStatus, ModelDeploymentInfo
)

# Workflow orchestration models (includes centralized prompt flows models)
from .workflow import (
    WorkflowContext, WorkflowResult, NodeExecution,
    TemplateConfig, TemplateRenderResult, FlowNode, WorkflowExecution,
    PromptContext, ComposedPrompt
)

# Validation models
from .validation import ValidationResult, ConfigValidation

# Workflow and system enumerations
from .enums import FlowType, FlowStatus

__all__ = [
    # Domain models
    "DomainConfig",
    "CorpusAnalysis", 
    "DomainStatistics",
    "DomainDiscovery",
    
    # Knowledge models
    "KnowledgeExtraction",
    "EntityResult",
    "RelationshipResult", 
    "KnowledgeValidation",
    
    # Search models
    "SearchRequest",
    "SearchResponse", 
    "SearchResults",
    "SearchMetrics",
    
    # Azure models (Core)
    "AzureServiceResponse",
    "EmbeddingResult",
    "SearchResult",
    "ServiceHealth",
    
    # Azure models (ML)
    "GNNTrainingConfig",
    "TrainingJobStatus", 
    "ModelDeploymentInfo",
    
    # Workflow models (Core)
    "WorkflowContext",
    "WorkflowResult",
    "NodeExecution",
    
    # Workflow models (Prompt Flows - centralized from local definitions)
    "TemplateConfig",
    "TemplateRenderResult",
    "FlowNode", 
    "WorkflowExecution",
    "PromptContext",
    "ComposedPrompt",
    
    # Validation models
    "ValidationResult",
    "ConfigValidation",
    
    # Enumerations
    "FlowType",
    "FlowStatus",
]