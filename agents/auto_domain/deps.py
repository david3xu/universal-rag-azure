"""
Auto Domain Agent Dependencies

PydanticAI-compliant dependencies for domain analysis agents.
Using centralized models from models/agent_deps.py
"""

# Import from centralized models directory
from models.agent_deps import AutoDomainDeps

# Re-export for convenience
__all__ = ["AutoDomainDeps"]