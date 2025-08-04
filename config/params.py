"""
Centralized Parameter Registry
Distinguishes infrastructure config from business logic that must be learned.
"""

from typing import Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum


class ParameterType(Enum):
    """Types of parameters in the system."""
    INFRASTRUCTURE = "infrastructure"  # Can be configured
    BUSINESS_LOGIC = "business_logic"   # MUST be learned
    PERFORMANCE = "performance"         # MUST be learned from metrics


@dataclass
class ParameterDefinition:
    """Definition of a system parameter."""
    name: str
    parameter_type: ParameterType
    description: str
    must_be_learned: bool
    default_source: Optional[str] = None


class ConfigurationNotAvailableError(Exception):
    """Raised when required learned configuration is not available."""
    pass


class CentralizedParameters:
    """Registry of all system parameters with learning requirements."""
    
    # INFRASTRUCTURE PARAMETERS - These can have configured defaults
    INFRASTRUCTURE_PARAMS = {
        "api_port": ParameterDefinition(
            "api_port", ParameterType.INFRASTRUCTURE,
            "API server port", False, "environment"
        ),
        "api_version": ParameterDefinition(
            "api_version", ParameterType.INFRASTRUCTURE, 
            "API version string", False, "environment"
        ),
        "log_level": ParameterDefinition(
            "log_level", ParameterType.INFRASTRUCTURE,
            "Logging level", False, "environment"
        ),
        "azure_region": ParameterDefinition(
            "azure_region", ParameterType.INFRASTRUCTURE,
            "Azure deployment region", False, "environment"
        ),
        "max_concurrent_requests": ParameterDefinition(
            "max_concurrent_requests", ParameterType.INFRASTRUCTURE,
            "Maximum concurrent API requests", False, "environment"
        ),
        "cache_category_dir": ParameterDefinition(
            "cache_category_dir", ParameterType.INFRASTRUCTURE,
            "Cache category directory name", False, "environment"
        ),
        "default_source_path": ParameterDefinition(
            "default_source_path", ParameterType.INFRASTRUCTURE,
            "Default source data path", False, "environment"
        ),
        "default_export_format": ParameterDefinition(
            "default_export_format", ParameterType.INFRASTRUCTURE,
            "Default export format for knowledge graphs", False, "environment"
        ),
    }
    
    # BUSINESS LOGIC PARAMETERS - These MUST be learned
    BUSINESS_LOGIC_PARAMS = {
        "default_domain": ParameterDefinition(
            "default_domain", ParameterType.BUSINESS_LOGIC,
            "Default domain for processing when not auto-detected", True, "domain_analysis"
        ),
        "similarity_threshold": ParameterDefinition(
            "similarity_threshold", ParameterType.BUSINESS_LOGIC,
            "Vector similarity threshold for search", True, "domain_analysis"
        ),
        "hop_count": ParameterDefinition(
            "hop_count", ParameterType.BUSINESS_LOGIC,
            "Graph traversal hop count", True, "domain_analysis"
        ),
        "max_results": ParameterDefinition(
            "max_results", ParameterType.BUSINESS_LOGIC,
            "Maximum search results to return", True, "domain_analysis"
        ),
        "vector_weight": ParameterDefinition(
            "vector_weight", ParameterType.BUSINESS_LOGIC,
            "Vector search modality weight", True, "domain_analysis"
        ),
        "graph_weight": ParameterDefinition(
            "graph_weight", ParameterType.BUSINESS_LOGIC,
            "Graph search modality weight", True, "domain_analysis"
        ),
        "gnn_weight": ParameterDefinition(
            "gnn_weight", ParameterType.BUSINESS_LOGIC,
            "GNN modality weight", True, "domain_analysis"
        ),
        "confidence_threshold": ParameterDefinition(
            "confidence_threshold", ParameterType.BUSINESS_LOGIC,
            "Minimum confidence for results", True, "domain_analysis"
        ),
        "entity_threshold": ParameterDefinition(
            "entity_threshold", ParameterType.BUSINESS_LOGIC,
            "Entity extraction confidence threshold", True, "domain_analysis"
        ),
        "relationship_threshold": ParameterDefinition(
            "relationship_threshold", ParameterType.BUSINESS_LOGIC,
            "Relationship extraction confidence threshold", True, "domain_analysis"
        ),
        "chunk_size": ParameterDefinition(
            "chunk_size", ParameterType.BUSINESS_LOGIC,
            "Document chunking size", True, "domain_analysis"
        ),
    }
    
    # PERFORMANCE PARAMETERS - These MUST be learned from system behavior
    PERFORMANCE_PARAMS = {
        "cache_hit_rate_target": ParameterDefinition(
            "cache_hit_rate_target", ParameterType.PERFORMANCE,
            "Target cache hit rate", True, "performance_learning"
        ),
        "response_time_target": ParameterDefinition(
            "response_time_target", ParameterType.PERFORMANCE,
            "Target response time in seconds", True, "performance_learning"
        ),
        "accuracy_target": ParameterDefinition(
            "accuracy_target", ParameterType.PERFORMANCE,
            "Target search accuracy", True, "performance_learning"
        ),
        "precision_target": ParameterDefinition(
            "precision_target", ParameterType.PERFORMANCE,
            "Target precision score", True, "performance_learning"
        ),
        "recall_target": ParameterDefinition(
            "recall_target", ParameterType.PERFORMANCE,
            "Target recall score", True, "performance_learning"
        ),
        "handshake_latency_limit": ParameterDefinition(
            "handshake_latency_limit", ParameterType.PERFORMANCE,
            "Maximum handshake latency", True, "performance_learning"
        ),
        "feedback_loop_speed_limit": ParameterDefinition(
            "feedback_loop_speed_limit", ParameterType.PERFORMANCE,
            "Maximum feedback loop response time", True, "performance_learning"
        ),
    }
    
    @classmethod
    def get_parameter_definition(cls, param_name: str) -> Optional[ParameterDefinition]:
        """Get parameter definition by name."""
        all_params = {
            **cls.INFRASTRUCTURE_PARAMS,
            **cls.BUSINESS_LOGIC_PARAMS, 
            **cls.PERFORMANCE_PARAMS
        }
        return all_params.get(param_name)
    
    @classmethod
    def must_be_learned(cls, param_name: str) -> bool:
        """Check if parameter must be learned (not hardcoded)."""
        param_def = cls.get_parameter_definition(param_name)
        return param_def.must_be_learned if param_def else True  # Default to requiring learning
    
    @classmethod
    def get_learning_source(cls, param_name: str) -> Optional[str]:
        """Get the required learning source for a parameter."""
        param_def = cls.get_parameter_definition(param_name)
        return param_def.default_source if param_def else None
    
    @classmethod
    def validate_parameter_usage(cls, param_name: str, value: Any, source: str) -> None:
        """Validate that parameter is being used correctly."""
        param_def = cls.get_parameter_definition(param_name)
        
        if not param_def:
            # Unknown parameter - require learning
            if source in ["hardcoded", "default", "fallback"]:
                raise ConfigurationNotAvailableError(
                    f"Unknown parameter '{param_name}' cannot use hardcoded value. "
                    f"Must be learned from domain analysis or performance data."
                )
            return
        
        if param_def.must_be_learned and source in ["hardcoded", "default", "fallback"]:
            raise ConfigurationNotAvailableError(
                f"Parameter '{param_name}' is {param_def.parameter_type.value} and must be learned "
                f"from {param_def.default_source}, not hardcoded. "
                f"Description: {param_def.description}"
            )
    
    @classmethod
    def get_all_required_learned_parameters(cls) -> Dict[str, ParameterDefinition]:
        """Get all parameters that must be learned."""
        learned_params = {}
        all_params = {
            **cls.INFRASTRUCTURE_PARAMS,
            **cls.BUSINESS_LOGIC_PARAMS,
            **cls.PERFORMANCE_PARAMS
        }
        
        for name, param_def in all_params.items():
            if param_def.must_be_learned:
                learned_params[name] = param_def
                
        return learned_params
    
    @classmethod
    def generate_learning_requirements_report(cls) -> str:
        """Generate report of all learning requirements."""
        learned_params = cls.get_all_required_learned_parameters()
        
        report = "# Learning Requirements Report\n\n"
        
        # Group by learning source
        by_source = {}
        for param_name, param_def in learned_params.items():
            source = param_def.default_source
            if source not in by_source:
                by_source[source] = []
            by_source[source].append((param_name, param_def))
        
        for source, params in by_source.items():
            report += f"## {source.replace('_', ' ').title()}\n\n"
            for param_name, param_def in params:
                report += f"- **{param_name}**: {param_def.description}\n"
            report += "\n"
            
        return report