# Ticket Analytics Dashboard

This directory contains a lightweight Streamlit dashboard for the ticket analytics project.

## Requirements

Install dependencies from the project root:

```bash
pip install -r requirements.txt
```

Key packages:

- `pandas`, `numpy`
- `matplotlib`, `plotly`
- `scikit-learn`
- `streamlit`
```

## Running the Dashboard

From the project root (`d:\\springboard_env`):

```bash
streamlit run dashboard/app.py
```

The app expects the feature-enriched dataset at:

- `data/processed/tickets_features.csv`

If it is missing, first run the Milestone 1 pipeline/notebook:

- `src/milestone1_pipeline.py` (executed via `notebooks/01_ticket_analytics_milestones.ipynb`)

## Features

- KPI cards:
  - **Avg Resolution Time (hours)**
  - **Most Frequent Category**
  - **Cluster Similarity Index** (from Module 4 reports)
  - **Top Region/Team**
- Filters:
  - Priority, Type, Category, Region, Team/Assignee, Cluster (when columns exist)
- Charts:
  - Resolution time by priority
  - Resolution time by ticket type
  - Ticket counts by category and queue
  - High-priority unresolved backlog (when `reports/high_priority_unresolved.csv` is available)

