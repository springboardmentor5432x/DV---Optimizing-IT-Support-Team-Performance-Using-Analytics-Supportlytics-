"""
Simple Streamlit dashboard for ticket analytics.

Run with:
    streamlit run dashboard/app.py
from the repository root.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

from src.schema import detect_schema


BASE_DIR = Path(__file__).resolve().parents[1]
FEATURES_PATH = BASE_DIR / "data" / "processed" / "tickets_features.csv"


@st.cache_data
def load_data() -> pd.DataFrame:
    if not FEATURES_PATH.exists():
        st.error(f"Features file not found at {FEATURES_PATH}. Run Milestone 1 pipeline first.")
        return pd.DataFrame()
    return pd.read_csv(FEATURES_PATH)


st.set_page_config(page_title="Ticket Analytics Dashboard", layout="wide")
st.title("Ticket Analytics Dashboard")

df = load_data()
if df.empty:
    st.stop()

schema = detect_schema(df)
st.sidebar.header("Filters")

# Sidebar filters based on detected schema
def sidebar_multiselect(label: str, col_name: str):
    if not col_name or col_name not in df.columns:
        return None
    options = sorted(df[col_name].dropna().astype(str).unique().tolist())
    selected = st.sidebar.multiselect(label, options, default=options)
    if not selected:
        return df
    return df[df[col_name].astype(str).isin(selected)]

filtered = df.copy()
for label, key in [
    ("Priority", schema.priority),
    ("Type", schema.type),
    ("Category", schema.category),
    ("Region", schema.region or schema.country),
    ("Team/Assignee", schema.team),
    ("Cluster", schema.cluster_id),
]:
    if key and key in filtered.columns:
        f = sidebar_multiselect(label, key)
        if f is not None:
            filtered = f

st.markdown("### KPI Overview")

res_col = "Resolution_Duration_Hours" if "Resolution_Duration_Hours" in filtered.columns else None
priority_col = schema.priority
category_col = schema.category
cluster_col = schema.cluster_id
region_col = schema.region or schema.country

col1, col2, col3, col4 = st.columns(4)

with col1:
    if res_col:
        avg_res = filtered[res_col].dropna()
        st.metric("Avg Resolution Time (hours)", f"{avg_res.mean():.2f}")
    else:
        st.metric("Avg Resolution Time (hours)", "N/A")

with col2:
    if category_col and category_col in filtered.columns:
        top_cat = filtered[category_col].value_counts().idxmax()
        st.metric("Most Frequent Category", top_cat)
    else:
        st.metric("Most Frequent Category", "N/A")

with col3:
    if cluster_col and cluster_col in filtered.columns:
        st.metric("Cluster Similarity Index", "See Module 4 report")
    else:
        st.metric("Cluster Similarity Index", "N/A")

with col4:
    if region_col and region_col in filtered.columns:
        top_region = filtered[region_col].value_counts().idxmax()
        st.metric("Top Region/Team", top_region)
    else:
        st.metric("Top Region/Team", "N/A")

st.markdown("---")

st.subheader("Resolution Time by Priority and Type")
if res_col and priority_col and priority_col in filtered.columns:
    grp = (
        filtered[[priority_col, res_col]]
        .dropna()
        .groupby(priority_col)[res_col]
        .mean()
        .sort_values(ascending=False)
    )
    st.bar_chart(grp)

if res_col and schema.type and schema.type in filtered.columns:
    grp2 = (
        filtered[[schema.type, res_col]]
        .dropna()
        .groupby(schema.type)[res_col]
        .mean()
        .sort_values(ascending=False)
        .head(15)
    )
    st.bar_chart(grp2)

st.subheader("Tickets by Category / Queue")
if category_col and category_col in filtered.columns:
    st.bar_chart(filtered[category_col].value_counts().head(15))
if schema.queue and schema.queue in filtered.columns:
    st.bar_chart(filtered[schema.queue].value_counts().head(15))

st.subheader("High-Priority Unresolved Backlog")
backlog_path = BASE_DIR / "reports" / "high_priority_unresolved.csv"
if backlog_path.exists():
    backlog = pd.read_csv(backlog_path)
    st.dataframe(backlog.head(50))
else:
    st.info("High-priority unresolved export not found. See Day 3 section in `Progress.ipynb`.")

