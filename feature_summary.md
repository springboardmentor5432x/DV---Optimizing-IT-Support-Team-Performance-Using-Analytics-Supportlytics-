# Feature Engineering Summary (Milestone 1)

## Cleaning Steps
- Removed duplicate rows
- Stripped whitespace from text columns
- Parsed created/resolved dates (if present)
- Filled missing values in key categorical columns (Type/Priority/Category) with `Unknown`

## New Features
- `Resolution_Duration_Hours`: Calculated as (Resolved Date - Created Date) in hours (if both columns exist)
- `Priority_Score`: Mapped priority text to numeric score (Critical=4, High=3, Medium=2, Low=1)
