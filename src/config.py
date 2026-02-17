"""
Project-wide configuration and constants.

This module centralizes:
- Priority score mappings
- Default clustering parameters
"""

from typing import Dict


# Priority label -> numeric score
# Used throughout feature engineering and analytics.
PRIORITY_SCORE_MAP: Dict[str, int] = {
    "critical": 4,
    "high": 3,
    "medium": 2,
    "low": 1,
}


# Fallback score for unknown priority labels (e.g. "Urgent", "P1").
UNKNOWN_PRIORITY_SCORE: int = 2


# Default number of text clusters when no cluster_id column exists.
DEFAULT_N_CLUSTERS: int = 6


# Maximum number of document pairs sampled per cluster when estimating
# average cosine similarity (to keep computation light on large clusters).
MAX_SIMILARITY_PAIRS_PER_CLUSTER: int = 2000


