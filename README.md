📁 README — Week 1 & Week 2 (Module-1 & Module-2)
Week 1 — Dataset Understanding & Requirement Analysis

Explored the support ticket dataset

Identified key entities (ticket, customer, product, performance fields)

Mapped project objectives to dataset fields

Determined KPIs for analysis (Resolution Time, Priority, Ticket Status, Workload)

Classified columns into core, optional, and removable

Defined problem scope: IT Support Ticket Performance Analysis

Week 2 — Data Preprocessing & Feature Engineering

Loaded and cleaned raw dataset

Removed PII/irrelevant fields (name, email, resolution text, channel)

Converted timestamps to datetime format

Encoded ticket priority into numerical score

Engineered Resolution Time (Hours) as primary performance KPI

Created unresolved & unresponded ticket flags

Categorized resolution speed (Fast / Medium / Slow)

Handled missing values logically (pending/unresolved cases preserved)

Exported preprocessed dataset for EDA phase

Output of Module-2

Clean & structured EDA-ready dataset
processed_support_tickets.csv (.xlsx)
