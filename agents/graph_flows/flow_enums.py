"""
Flow Enums

Enumerations for workflow flows.
"""

from enum import Enum


class FlowType(Enum):
    """Types of workflow flows."""
    # TODO: Add comprehensive flow type definitions for dual-graph architecture
    # TODO: Include workflow communication and handshake flow types
    # TODO: Add error handling and recovery flow types
    # TODO: Include performance monitoring and optimization flows
    # TODO: Add configuration learning and adaptation flow types
    DOMAIN_CONFIG = "domain_config"
    SEARCH = "search"
    KNOWLEDGE_EXTRACTION = "knowledge_extraction"


class FlowStatus(Enum):
    """Status of workflow flows."""
    # TODO: Add detailed status tracking for workflow states
    # TODO: Include intermediate status states for progress tracking
    # TODO: Add error substatus for different failure types
    # TODO: Include recovery and retry status indicators
    # TODO: Add performance and quality status metrics
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class ConfigSource(Enum):
    """Sources of configuration."""
    # TODO: Add comprehensive configuration source tracking
    # TODO: Include learned configuration source with confidence levels
    # TODO: Add cached configuration source with freshness indicators
    # TODO: Include hybrid configuration sources (learned + validated)
    # TODO: Add configuration source validation and trust levels
    WORKFLOW_GENERATED = "workflow_generated"
    DOMAIN_ANALYSIS = "domain_analysis" 
    USER_PROVIDED = "user_provided"


class CommunicationType(Enum):
    """Types of inter-workflow communication."""
    # TODO: Define handshake protocol types for workflow initialization
    # TODO: Add configuration negotiation communication types
    # TODO: Include performance feedback communication patterns
    # TODO: Add error reporting and recovery communication types
    # TODO: Include status broadcasting and health check communications
    HANDSHAKE = "handshake"
    CONFIG_REQUEST = "config_request"
    CONFIG_RESPONSE = "config_response"
    PERFORMANCE_FEEDBACK = "performance_feedback"
    ERROR_NOTIFICATION = "error_notification"
    STATUS_UPDATE = "status_update"


class MessagePriority(Enum):
    """Priority levels for workflow messages."""
    # TODO: Define message priority system for efficient workflow communication
    # TODO: Add urgent priority for error handling and system recovery
    # TODO: Include normal priority for standard workflow operations
    # TODO: Add low priority for optimization and background tasks
    # TODO: Include system priority for critical infrastructure messages
    URGENT = "urgent"
    HIGH = "high"
    NORMAL = "normal"
    LOW = "low"
    BACKGROUND = "background"


class WorkflowState(Enum):
    """States of workflow execution and communication."""
    # TODO: Define comprehensive workflow state machine
    # TODO: Add initialization and readiness check states
    # TODO: Include active communication and negotiation states
    # TODO: Add completed and cleanup states
    # TODO: Include error, recovery, and shutdown states
    INITIALIZING = "initializing"
    READY = "ready"
    NEGOTIATING = "negotiating"
    EXECUTING = "executing"
    COMMUNICATING = "communicating"
    COMPLETED = "completed"
    ERROR = "error"
    RECOVERING = "recovering"
    SHUTDOWN = "shutdown"


class QualityMetric(Enum):
    """Quality metrics for workflow execution."""
    # TODO: Define comprehensive quality measurement framework
    # TODO: Add configuration generation quality metrics
    # TODO: Include search result quality and relevance metrics
    # TODO: Add communication efficiency and reliability metrics
    # TODO: Include performance optimization and learning metrics
    CONFIG_COMPLETENESS = "config_completeness"
    CONFIG_ACCURACY = "config_accuracy"
    SEARCH_RELEVANCE = "search_relevance"
    SEARCH_COVERAGE = "search_coverage"
    COMMUNICATION_EFFICIENCY = "communication_efficiency"
    LEARNING_EFFECTIVENESS = "learning_effectiveness"