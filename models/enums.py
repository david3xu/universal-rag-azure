"""
Workflow and Flow Enumerations

Centralized enumerations for workflow flows and system states.
"""

from enum import Enum


class FlowType(Enum):
    """Basic flow types - simplified for core functionality."""
    # TODO: Add basic flow type definitions
    # TODO: Include domain and search flow types
    pass


class FlowStatus(Enum):
    """Basic flow status - simplified for core functionality."""
    # TODO: Add basic status tracking for workflows
    # TODO: Include pending, active, completed, error states
    pass

# =============================================================================
# TEMPORARILY COMMENTED OUT ADVANCED FEATURES
# These will be re-enabled once basic functionality is working
# =============================================================================

# class ConfigSource(Enum):
#     """Sources of configuration."""
#     # TODO: Add comprehensive configuration source tracking
#     # TODO: Include learned configuration source with confidence levels
#     # TODO: Add cached configuration source with freshness indicators
#     # TODO: Include hybrid configuration sources (learned + validated)
#     # TODO: Add configuration source validation and trust levels
#     pass

# class CommunicationType(Enum):
#     """Types of inter-workflow communication."""
#     # TODO: Define handshake protocol types for workflow initialization
#     # TODO: Add configuration negotiation communication types
#     # TODO: Include performance feedback communication patterns
#     # TODO: Add error reporting and recovery communication types
#     # TODO: Include status broadcasting and health check communications
#     pass

# class MessagePriority(Enum):
#     """Priority levels for workflow messages."""
#     # TODO: Define message priority system for efficient workflow communication
#     # TODO: Add urgent priority for error handling and system recovery
#     # TODO: Include normal priority for standard workflow operations
#     # TODO: Add low priority for optimization and background tasks
#     # TODO: Include system priority for critical infrastructure messages
#     pass

# class WorkflowState(Enum):
#     """States of workflow execution and communication."""
#     # TODO: Define comprehensive workflow state machine
#     # TODO: Add initialization and readiness check states
#     # TODO: Include active communication and negotiation states
#     # TODO: Add completed and cleanup states
#     # TODO: Include error, recovery, and shutdown states
#     pass

# class QualityMetric(Enum):
#     """Quality metrics for workflow execution."""
#     # TODO: Define comprehensive quality measurement framework
#     # TODO: Add configuration generation quality metrics
#     # TODO: Include search result quality and relevance metrics
#     # TODO: Add communication efficiency and reliability metrics
#     # TODO: Include performance optimization and learning metrics
#     pass