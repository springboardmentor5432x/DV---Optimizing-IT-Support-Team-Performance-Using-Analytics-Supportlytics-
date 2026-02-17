import os
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from src.schema import detect_schema
from src.config import PRIORITY_SCORE_MAP, UNKNOWN_PRIORITY_SCORE

# -----------------------------
# CONFIG
# -----------------------------
# Project root inferred from this file location, so relative paths
# work regardless of current working directory.
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "raw" / "customer_support_tickets.csv"
OUT_CLEAN_DIR = BASE_DIR / "data" / "processed"
OUT_VIS_DIR = BASE_DIR / "outputs" / "figures"
DOCS_DIR = BASE_DIR / "reports"

os.makedirs(OUT_CLEAN_DIR, exist_ok=True)
os.makedirs(OUT_VIS_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)

# -----------------------------
# 1) LOAD DATA
# -----------------------------
df = pd.read_csv(DATA_PATH)

# Basic info prints (for your mentor)
print("Rows, Cols:", df.shape)
print("\nColumns:\n", df.columns.tolist())
print("\nDtypes:\n", df.dtypes)
print("\nMissing values (top 25):\n", df.isna().sum().sort_values(ascending=False).head(25))

# Save schema + missing report
schema_report_path = os.path.join(DOCS_DIR, "schema_missing_report.txt")
with open(schema_report_path, "w", encoding="utf-8") as f:
    f.write(f"Shape: {df.shape}\n\n")
    f.write("Columns:\n" + "\n".join(df.columns.astype(str)) + "\n\n")
    f.write("Dtypes:\n" + df.dtypes.to_string() + "\n\n")
    f.write("Missing values:\n" + df.isna().sum().sort_values(ascending=False).to_string() + "\n")

# -----------------------------
# 2) FIND CANDIDATE COLUMNS (via schema mapping)
# -----------------------------
schema = detect_schema(df)
col_type = schema.type
col_priority = schema.priority
col_category = schema.category
col_created = schema.created_date
col_resolved = schema.resolved_date

print("\nDetected columns (schema):")
print("Type:", col_type)
print("Priority:", col_priority)
print("Category:", col_category)
print("Created:", col_created)
print("Resolved:", col_resolved)

# -----------------------------
# 3) INITIAL DISTRIBUTIONS (Module 1)
# -----------------------------
def save_bar(series, title, filename, top_n=15):
    s = series.dropna().astype(str).str.strip()
    vc = s.value_counts().head(top_n)
    plt.figure()
    vc.sort_values().plot(kind="bar")
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_VIS_DIR, filename), dpi=200)
    plt.close()

if col_type:
    save_bar(df[col_type], "Ticket Distribution by Type", "ticket_type_distribution.png")
if col_priority:
    save_bar(df[col_priority], "Ticket Distribution by Priority", "priority_distribution.png")
if col_category:
    save_bar(df[col_category], "Ticket Distribution by Category (Top 15)", "category_distribution.png")

# -----------------------------
# 4) CLEANING (Module 2)
# -----------------------------
df_clean = df.copy()

# Drop exact duplicates
df_clean = df_clean.drop_duplicates()

# Strip text columns
for c in df_clean.columns:
    if df_clean[c].dtype == "object":
        df_clean[c] = df_clean[c].astype(str).str.strip().replace({"nan": np.nan, "None": np.nan})

# Parse dates if available
if col_created:
    df_clean[col_created] = pd.to_datetime(df_clean[col_created], errors="coerce")
if col_resolved:
    df_clean[col_resolved] = pd.to_datetime(df_clean[col_resolved], errors="coerce")

# Fill missing text fields lightly (keep it simple for milestone 1)
# Only fill for the key categorical columns so plots don't break
for c in [col_type, col_priority, col_category]:
    if c and c in df_clean.columns:
        df_clean[c] = df_clean[c].fillna("Unknown")

# -----------------------------
# 5) FEATURE ENGINEERING
# -----------------------------
# 5.1 Resolution Duration
if col_created and col_resolved:
    df_clean["Resolution_Duration_Hours"] = (
        (df_clean[col_resolved] - df_clean[col_created]).dt.total_seconds() / 3600.0
    )
else:
    df_clean["Resolution_Duration_Hours"] = np.nan  # dataset may not have both dates

# 5.2 Priority Score mapping
# (handles common labels via config; unknown -> UNKNOWN_PRIORITY_SCORE)
if col_priority:
    p_series = df_clean[col_priority].astype(str).str.lower().str.strip()
    df_clean["Priority_Score"] = p_series.map(PRIORITY_SCORE_MAP).fillna(UNKNOWN_PRIORITY_SCORE)
else:
    df_clean["Priority_Score"] = np.nan

# -----------------------------
# 6) SAVE CLEANED + FEATURES DATASET
# -----------------------------
clean_path = os.path.join(OUT_CLEAN_DIR, "tickets_cleaned.csv")
features_path = os.path.join(OUT_CLEAN_DIR, "tickets_features.csv")

# Save cleaned before feature additions (if needed later)
df_basic = df_clean.drop(columns=["Resolution_Duration_Hours", "Priority_Score"], errors="ignore")
df_basic.to_csv(clean_path, index=False)
df_clean.to_csv(features_path, index=False)
print("\nSaved cleaned dataset to:", clean_path)
print("Saved features dataset to:", features_path)

# -----------------------------
# 7) DATA DICTIONARY + FEATURE SUMMARY DOCS
# -----------------------------
# Data dictionary
dd_path = os.path.join(DOCS_DIR, "data_dictionary.md")
with open(dd_path, "w", encoding="utf-8") as f:
    f.write("# Data Dictionary\n\n")
    f.write("| Column | Type | Description |\n")
    f.write("|---|---|---|\n")
    for c in df_clean.columns:
        f.write(f"| `{c}` | `{str(df_clean[c].dtype)}` | TBD (fill as per dataset meaning) |\n")

# Feature summary
fs_path = os.path.join(DOCS_DIR, "feature_engineering_summary.md")
with open(fs_path, "w", encoding="utf-8") as f:
    f.write("# Feature Engineering Summary (Milestone 1)\n\n")
    f.write("## Cleaning Steps\n")
    f.write("- Removed duplicate rows\n")
    f.write("- Stripped whitespace from text columns\n")
    f.write("- Parsed created/resolved dates (if present)\n")
    f.write("- Filled missing values in key categorical columns (Type/Priority/Category) with `Unknown`\n\n")
    f.write("## New Features\n")
    f.write("- `Resolution_Duration_Hours`: Calculated as (Resolved Date - Created Date) in hours (if both columns exist)\n")
    f.write("- `Priority_Score`: Mapped priority text to numeric score (Critical=4, High=3, Medium=2, Low=1)\n")

print("\nDocs saved:", dd_path, fs_path)
print("\nCharts saved to:", OUT_VIS_DIR)
