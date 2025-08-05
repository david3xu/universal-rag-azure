"""
Centralized Parameter Registry
Distinguishes infrastructure config from business logic that must be learned.
"""

from typing import Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum


class ConfigurationNotAvailableError(Exception):
    """Raised when required learned configuration is not available."""
    pass


class CentralizedParameters:
    """Registry of all system parameters with learning requirements."""
    
    def __init__(self):
        """Initialize basic parameter registry."""
        # TODO: Initialize basic parameter tracking for anti-hardcoding
        # TODO: Set up simple parameter validation
        pass
    
    @classmethod
    def must_be_learned(cls, param_name: str) -> bool:
        """Check if parameter must be learned (not hardcoded) - basic version."""
        # TODO: Basic check if parameter should be learned vs hardcoded
        # TODO: Default to requiring learning for unknown parameters (anti-hardcoding principle)
        pass
    
# =============================================================================
# TEMPORARILY COMMENTED OUT ADVANCED FEATURES
# These will be re-enabled once basic functionality is working
# =============================================================================

# class ParameterType(Enum):
#     """Types of parameters in the system."""
#     # TODO: Define infrastructure parameter type
#     # TODO: Define business logic parameter type
#     # TODO: Define performance parameter type
#     pass

# @dataclass
# class ParameterDefinition:
#     """Definition of a system parameter."""
#     # TODO: Define parameter name field
#     # TODO: Define parameter type field
#     # TODO: Define description field
#     # TODO: Define must_be_learned field
#     # TODO: Define default_source field
#     pass

#     @classmethod
#     def get_parameter_definition(cls, param_name: str) -> Optional[ParameterDefinition]:
#         """Get parameter definition by name."""
#         # TODO: Implement parameter definition lookup
#         # TODO: Search across all parameter categories
#         # TODO: Return parameter definition or None
#         pass

#     @classmethod
#     def get_learning_source(cls, param_name: str) -> Optional[str]:
#         """Get the required learning source for a parameter."""
#         # TODO: Get parameter definition
#         # TODO: Return default_source if available
#         # TODO: Return None for unknown parameters
#         pass
    
#     @classmethod
#     def validate_parameter_usage(cls, param_name: str, value: Any, source: str) -> None:
#         """Validate that parameter is being used correctly."""
#         # TODO: Get parameter definition
#         # TODO: Check if unknown parameter uses hardcoded value
#         # TODO: Validate learned parameters don't use hardcoded sources
#         # TODO: Raise ConfigurationNotAvailableError for violations
#         pass
    
#     @classmethod
#     def get_all_required_learned_parameters(cls) -> Dict[str, ParameterDefinition]:
#         """Get all parameters that must be learned."""
#         # TODO: Iterate through all parameter categories
#         # TODO: Filter parameters that must be learned
#         # TODO: Return dictionary of learned parameters
#         pass
    
#     @classmethod
#     def generate_learning_requirements_report(cls) -> str:
#         """Generate report of all learning requirements."""
#         # TODO: Get all required learned parameters
#         # TODO: Group parameters by learning source
#         # TODO: Generate formatted report
#         # TODO: Return comprehensive learning requirements report
#         pass