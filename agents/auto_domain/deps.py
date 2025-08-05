"""
Auto Domain Agent Dependencies

PydanticAI-compliant dependencies for domain analysis agents.
"""

from typing import Optional, Any
from pydantic import BaseModel, Field


class AutoDomainDeps(BaseModel):
    """Dependencies for Auto Domain Agent - PydanticAI compliant."""
    
    # Azure services integration
    azure_services: Optional[Any] = Field(
        default=None,
        description="Azure services container for storage, OpenAI, etc."
    )
    
    # Analysis components
    corpus_analyzer: Optional[Any] = Field(
        default=None,
        description="Corpus analyzer for document analysis"
    )
    
    config_builder: Optional[Any] = Field(
        default=None,
        description="Configuration builder for domain config generation"
    )
    
    pattern_learner: Optional[Any] = Field(
        default=None,
        description="Pattern learner for semantic analysis"
    )
    
    # Performance tracking
    performance_monitor: Optional[Any] = Field(
        default=None,
        description="Performance monitoring and metrics"
    )
    
    class Config:
        arbitrary_types_allowed = True
        extra = "forbid"