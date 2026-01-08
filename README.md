#Module 1 — Dataset Understanding & Preparation

Imported raw customer support ticket dataset

Identified key fields related to ticket handling and performance

Classified columns by roles (core, optional, drop)

Removed PII fields (Customer Name, Email)

Retained core performance fields (Status, Priority, Time fields)

Validated domain concepts (Ticket lifecycle, unresolved tickets, priority levels)

Defined project KPIs (Resolution Time, Unresolved/Unresponded flags, Priority)

#Module 2 — Data Cleaning & Feature Engineering

Converted date/time columns to standardized datetime format

Encoded priority into numeric Priority Score

Engineered Resolution Time (Hours) from timestamps

Created binary flags for Unresolved and Unresponded tickets

Categorized resolution speed (Fast/Medium/Slow)

Handled missing time values as valid unresolved cases

Exported cleaned dataset for EDA (processed_support_tickets.csv/.xlsx)
