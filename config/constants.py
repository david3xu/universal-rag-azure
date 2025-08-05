"""
Centralized Configuration Constants

Centralized constants for configuration generation algorithms.
These are ALGORITHM CONSTANTS, not business configuration values.
"""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass(frozen=True)
class CorpusAnalysisConstants:
    """Constants for corpus analysis algorithms."""
    
    # Document count thresholds for classification
    SMALL_CORPUS_THRESHOLD: int = 50      # Below this = small corpus
    MEDIUM_CORPUS_THRESHOLD: int = 200    # Above this = large corpus
    
    # Document length analysis
    SHORT_DOC_THRESHOLD: int = 500        # Tokens - below this = short docs
    LONG_DOC_THRESHOLD: int = 2000        # Tokens - above this = long docs
    
    # Basic statistical analysis bounds
    MIN_VOCABULARY_DIVERSITY: float = 0.1    # Minimum expected vocabulary diversity
    MAX_VOCABULARY_DIVERSITY: float = 0.9    # Maximum expected vocabulary diversity


@dataclass(frozen=True)
class ConfigGenerationConstants:
    """Constants for configuration value generation algorithms."""
    
    # Similarity threshold generation bounds
    MIN_SIMILARITY_THRESHOLD: float = 0.5    # Minimum viable similarity threshold
    MAX_SIMILARITY_THRESHOLD: float = 0.95   # Maximum practical similarity threshold
    DEFAULT_SIMILARITY_BASE: float = 0.7     # Base threshold for medium corpora
    
    # Result limits generation bounds
    MIN_RESULTS_LIMIT: int = 5               # Minimum useful result count
    MAX_RESULTS_LIMIT: int = 50              # Maximum practical result count
    RESULTS_PER_DOC_RATIO: float = 0.1       # Results as fraction of document count
    
    # Tri-modal weight defaults (equal distribution)
    DEFAULT_VECTOR_WEIGHT: float = 0.33      # Default vector search weight
    DEFAULT_GRAPH_WEIGHT: float = 0.33       # Default graph search weight  
    DEFAULT_GNN_WEIGHT: float = 0.34         # Default GNN search weight
    
    # Performance target defaults
    DEFAULT_RESPONSE_TIME_TARGET: float = 2.0    # Default response time target (seconds)
    DEFAULT_CACHE_TTL: int = 3600                 # Default cache TTL (1 hour)


@dataclass(frozen=True)
class QualityThresholdConstants:
    """Constants for quality threshold generation."""
    
    # Extraction quality bounds
    MIN_EXTRACTION_QUALITY: float = 0.6      # Minimum acceptable extraction quality
    DEFAULT_EXTRACTION_QUALITY: float = 0.8  # Default extraction quality threshold
    
    # Search relevance bounds
    MIN_SEARCH_RELEVANCE: float = 0.5        # Minimum acceptable search relevance
    DEFAULT_SEARCH_RELEVANCE: float = 0.75   # Default search relevance threshold
    
    # Confidence thresholds
    MIN_ENTITY_CONFIDENCE: float = 0.6       # Minimum entity extraction confidence
    DEFAULT_ENTITY_CONFIDENCE: float = 0.75  # Default entity confidence threshold
    MIN_RELATIONSHIP_CONFIDENCE: float = 0.6  # Minimum relationship confidence
    DEFAULT_RELATIONSHIP_CONFIDENCE: float = 0.7  # Default relationship confidence


@dataclass(frozen=True)
class AlgorithmConstants:
    """Constants for configuration generation algorithms."""
    
    # Scaling factors for corpus size influence
    CORPUS_SIZE_INFLUENCE_FACTOR: float = 0.2    # How much corpus size affects thresholds
    DOC_LENGTH_INFLUENCE_FACTOR: float = 0.1     # How much doc length affects thresholds
    
    # Boundary conditions
    MIN_DOCS_FOR_RELIABLE_STATS: int = 10        # Minimum docs needed for reliable statistics
    CONFIDENCE_DECAY_FACTOR: float = 0.9         # Confidence reduction for small corpora


# Singleton instances for easy access
CORPUS_CONSTANTS = CorpusAnalysisConstants()
CONFIG_CONSTANTS = ConfigGenerationConstants()
QUALITY_CONSTANTS = QualityThresholdConstants()
ALGORITHM_CONSTANTS = AlgorithmConstants()


def get_all_constants() -> Dict[str, Any]:
    """Get all constants for debugging and validation."""
    return {
        "corpus_analysis": CORPUS_CONSTANTS.__dict__,
        "config_generation": CONFIG_CONSTANTS.__dict__,
        "quality_thresholds": QUALITY_CONSTANTS.__dict__,
        "algorithms": ALGORITHM_CONSTANTS.__dict__
    }


def validate_constants() -> bool:
    """Validate that all constants are within reasonable bounds."""
    # Validate similarity thresholds
    assert 0.0 <= CONFIG_CONSTANTS.MIN_SIMILARITY_THRESHOLD <= CONFIG_CONSTANTS.MAX_SIMILARITY_THRESHOLD <= 1.0
    
    # Validate result limits
    assert CONFIG_CONSTANTS.MIN_RESULTS_LIMIT > 0
    assert CONFIG_CONSTANTS.MIN_RESULTS_LIMIT <= CONFIG_CONSTANTS.MAX_RESULTS_LIMIT
    
    # Validate tri-modal weights sum to 1.0
    weight_sum = (CONFIG_CONSTANTS.DEFAULT_VECTOR_WEIGHT + 
                  CONFIG_CONSTANTS.DEFAULT_GRAPH_WEIGHT + 
                  CONFIG_CONSTANTS.DEFAULT_GNN_WEIGHT)
    assert abs(weight_sum - 1.0) < 0.01  # Allow small floating point errors
    
    # Validate quality thresholds
    assert 0.0 <= QUALITY_CONSTANTS.MIN_EXTRACTION_QUALITY <= QUALITY_CONSTANTS.DEFAULT_EXTRACTION_QUALITY <= 1.0
    assert 0.0 <= QUALITY_CONSTANTS.MIN_SEARCH_RELEVANCE <= QUALITY_CONSTANTS.DEFAULT_SEARCH_RELEVANCE <= 1.0
    
    return True


# Validate constants on import
validate_constants()