# Ticket Analytics Project

End-to-end analytics pipeline for customer support tickets, organized by milestones.

## Setup

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Ensure the raw dataset is available at:

```text
data/raw/customer_support_tickets.csv
```

If not, copy `customer_support_tickets.csv` from the project root into `data/raw/`.

## Project Structure

- `data/raw/` – raw CSVs (e.g., `customer_support_tickets.csv`)
- `data/processed/` – cleaned and feature-enriched datasets
- `src/` – reusable code (schema detection, config, pipelines)
- `notebooks/` – Jupyter notebooks (milestone orchestration)
- `reports/` – markdown reports, gap analysis, performance summaries
- `outputs/figures/` – saved plots
- `outputs/visuals/` – legacy plots from earlier exploration
- `dashboard/` – Streamlit dashboard

## Running the Analysis Notebook

Main orchestrator notebook:

```text
notebooks/01_ticket_analytics_milestones.ipynb
```

Recommended workflow:

1. Open the notebook in Jupyter/VSCode/Cursor.
2. Run all cells from top to bottom on a fresh kernel.
3. This will:
   - Load the raw CSV
   - Detect schema/column mappings
   - Run Milestone 1 cleaning & feature engineering (`src/milestone1_pipeline.py`)
   - Produce processed datasets under `data/processed/`
   - Generate the core visualizations under `outputs/figures/`

Additional, more detailed exploratory work is kept in:

```text
Progress.ipynb
```

## Running the Dashboard

From the project root:

```bash
streamlit run dashboard/app.py
```

The dashboard reads:

- `data/processed/tickets_features.csv`
- `reports/high_priority_unresolved.csv` (for backlog view)

Ensure you have run the Milestone 1 notebook/pipeline first so these files exist.

## Reports

Key reports:

- `reports/milestone_gap_report.md` – status vs milestone checklist
- `reports/feature_engineering_summary.md` – cleaning & feature engineering notes
- `reports/data_dictionary.md` – column-level documentation
- `reports/performance_metrics_summary.md` – KPIs and performance views
- `reports/visualization_index.md` – catalog of generated visualizations

