📊 Support Ticket Performance & Geographic Analysis
🚀 Project Overview

This project analyzes IT support ticket data to evaluate operational efficiency, workload distribution, regional performance, and high-priority handling using Python (EDA & Clustering) and Power BI (Dashboard & DAX).
The objective is to transform raw ticket data into actionable business insights through interactive visualization and analytical modeling.

📌 Milestone 1: Data Collection & Understanding
🎯 Objective
Understand the structure and characteristics of the support ticket dataset.

🔍 Activities Performed
Imported dataset into Python and Power BI
Explored key fields:
ticket_id
issue_category
ticket_type
priority_level
resolution_duration
region
Checked for missing values and inconsistencies
Generated realistic created_date and resolved_date for time-based analysis

✅ Outcome
Clean, structured dataset ready for analysis.

📌 Milestone 2: Data Preprocessing & Feature Engineering
🎯 Objective

Enhance dataset for advanced analytics.

🔧 Activities Performed
Converted resolution duration to numeric format
Created time-based features (Month, Date)
Applied KMeans Clustering to group similar tickets
Assigned cluster labels for operational segmentation

📊 Techniques Used
Data Cleaning
Feature Engineering
Clustering (KMeans)

✅ Outcome
Enriched dataset with cluster insights for performance comparison.

📌 Milestone 3: Exploratory Data Analysis (EDA)
🎯 Objective
Identify trends, patterns, and performance gaps.

📈 Analysis Conducted
Ticket distribution by Priority
Category frequency analysis
Region-wise performance comparison
Cluster size vs resolution time relationship

🔎 Key Insights
High-priority tickets contribute significantly to workload
Performance varies across regions
Some clusters show higher resolution duration (potential bottlenecks)

✅ Outcome
Identified operational inefficiencies and performance trends.

📌 Milestone 4: Dashboard Development (Power BI)
🎯 Objective
Build an interactive business intelligence dashboard.

📊 Key DAX Measures Created
1️⃣ Average Resolution Time
Avg Resolution Time =
AVERAGE(support_tickets_with_regions[resolution_duration])

2️⃣ Total Tickets
Total Tickets =
COUNT(support_tickets_with_regions[ticket_id])

3️⃣ High-Priority Tickets
High Priority Tickets =
CALCULATE(
    COUNT(support_tickets_with_regions[ticket_id]),
    support_tickets_with_regions[priority_level] = "High"
)

4️⃣ Top Performing Region
Dynamically identifies lowest average resolution time

📊 Visuals Used
KPI Cards (Performance Summary)
Bar Charts (Region & Cluster Comparison)
Pie Chart (Priority Distribution)
Scatter Plot (Cluster Size vs Performance)
Slicers (Region, Priority, Category, Date)

🎯 Business Impact
The dashboard helps management to:
Monitor operational efficiency
Identify high workload regions
Optimize resource allocation
Detect performance bottlenecks

🛠 Tools & Technologies
Python (Pandas, NumPy, Scikit-learn)
KMeans Clustering
Power BI
DAX (Data Analysis Expressions)
Data Visualization

📦 Final Deliverables
✅ Cleaned & Processed Dataset
✅ Clustering Analysis
✅ Exploratory Data Analysis
✅ Interactive Power BI Dashboard



✅ Presentation Slides

📌 Conclusion
