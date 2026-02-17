"""
Schema detection and column mapping utilities.

All analytics should rely on the logical names returned here instead of
hard-coding dataset column names. This makes the pipeline robust to
slight header / naming differences.
"""

from dataclasses import dataclass, asdict
from typing import Dict, List, Optional

import pandas as pd


@dataclass
class SchemaMapping:
    type: Optional[str] = None
    priority: Optional[str] = None
    category: Optional[str] = None
    queue: Optional[str] = None
    created_date: Optional[str] = None
    resolved_date: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    team: Optional[str] = None
    cluster_id: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    # One or more text fields used for NLP / similarity / clustering.
    text_fields: List[str] = None

    def as_dict(self) -> Dict[str, Optional[str]]:
        d = asdict(self)
        # text_fields is a list, keep as-is; others are scalars.
        return d


def _find_column(
    df: pd.DataFrame,
    preferred_exact: List[str],
    contains_keywords: Optional[List[str]] = None,
) -> Optional[str]:
    """Return first matching column by exact name or substring."""
    lower_map = {c.lower(): c for c in df.columns}

    for name in preferred_exact:
        if name.lower() in lower_map:
            return lower_map[name.lower()]

    if contains_keywords:
        for c in df.columns:
            cl = c.lower()
            for kw in contains_keywords:
                if kw.lower() in cl:
                    return c
    return None


def detect_schema(df: pd.DataFrame) -> SchemaMapping:
    """
    Detect likely columns for core concepts (type, priority, category, etc.).

    Returns a SchemaMapping. If a logical column cannot be found it is left as None.
    Downstream code should check for None and skip that analysis step gracefully.
    """
    # Type / issue type
    type_col = _find_column(
        df,
        preferred_exact=["Ticket Type", "Type", "Issue Type"],
        contains_keywords=["ticket type", "issue type", "type"],
    )

    # Priority
    priority_col = _find_column(
        df,
        preferred_exact=["Ticket Priority", "Priority", "Priority Level", "Urgency"],
        contains_keywords=["priority", "urgency"],
    )

    # Category / product / topic
    category_col = _find_column(
        df,
        preferred_exact=["Issue Category", "Category", "Product Category", "Product Purchased"],
        contains_keywords=["category", "product", "topic"],
    )

    # Queue / channel
    queue_col = _find_column(
        df,
        preferred_exact=["Queue", "Ticket Queue", "Ticket Channel", "Channel"],
        contains_keywords=["queue", "channel"],
    )

    # Created / opened date
    created_col = _find_column(
        df,
        preferred_exact=[
            "Created Date",
            "Created At",
            "Open Date",
            "Opened Date",
            "Ticket Created Date",
            "Date",
        ],
        contains_keywords=["created", "open", "opened", "date"],
    )

    # Resolved / closed date
    resolved_col = _find_column(
        df,
        preferred_exact=[
            "Resolved Date",
            "Resolved At",
            "Resolution Date",
            "Time to Resolution",
            "Closed Date",
            "Closed At",
        ],
        contains_keywords=["resolved", "resolution", "closed", "close"],
    )

    # Country / region
    country_col = _find_column(
        df,
        preferred_exact=["Country"],
        contains_keywords=["country"],
    )
    region_col = _find_column(
        df,
        preferred_exact=["Region"],
        contains_keywords=["region", "state", "province", "location"],
    )

    # Team / assignee
    team_col = _find_column(
        df,
        preferred_exact=["Team", "Assignee", "Owner", "Agent"],
        contains_keywords=["team", "assignee", "owner", "agent"],
    )

    # Cluster id if already present
    cluster_col = _find_column(
        df,
        preferred_exact=["cluster", "Cluster", "Cluster ID"],
        contains_keywords=["cluster"],
    )

    # Geo coordinates
    lat_col = _find_column(
        df,
        preferred_exact=["Latitude", "Lat"],
        contains_keywords=["latitude", "lat"],
    )
    lon_col = _find_column(
        df,
        preferred_exact=["Longitude", "Lon", "Lng"],
        contains_keywords=["longitude", "lon", "lng"],
    )

    # Text fields: consider typical subject/title/description columns
    text_candidates = []
    for c in df.columns:
        cl = c.lower()
        if any(k in cl for k in ["subject", "title", "description", "complaint", "issue", "text"]):
            text_candidates.append(c)
    # Deduplicate while preserving order
    seen = set()
    text_fields = []
    for c in text_candidates:
        if c not in seen:
            seen.add(c)
            text_fields.append(c)

    return SchemaMapping(
        type=type_col,
        priority=priority_col,
        category=category_col,
        queue=queue_col,
        created_date=created_col,
        resolved_date=resolved_col,
        country=country_col,
        region=region_col,
        team=team_col,
        cluster_id=cluster_col,
        latitude=lat_col,
        longitude=lon_col,
        text_fields=text_fields,
    )


