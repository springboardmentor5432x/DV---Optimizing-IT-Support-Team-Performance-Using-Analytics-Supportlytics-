# README — Milestone 1 (Module-1 & Module-2)
# Week 1 — Dataset Understanding & Requirement Analysis

Explored the support ticket dataset

Identified key entities (ticket, customer, product, performance fields)

Mapped project objectives to dataset fields

Determined KPIs for analysis (Resolution Time, Priority, Ticket Status, Workload)

Classified columns into core, optional, and removable

Defined problem scope: IT Support Ticket Performance Analysis

# Week 2 — Data Preprocessing & Feature Engineering

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

# Milestone 2 (Week 3 and 4).

# Module 3 — Exploratory Data Analysis (Week-3)

Objective:
To analyze support ticket behavior, workload, performance metrics, and backlog trends to uncover operational inefficiencies.

Key Work Done:

Performed dataset profiling and validation

Analyzed ticket workload distribution by:

Ticket Type

Ticket Priority

Ticket Status

Calculated unresolved vs resolved ticket ratios

Evaluated resolution performance (mean, median, variance)

Examined resolution category distribution (Fast/Slow)

Analyzed priority vs resolution time

Analyzed ticket type vs resolution time

Interpreted SLA compliance behavior

Identified performance bottlenecks and backlog trends

Visualizations Created (8+):

Ticket Type distribution

Priority distribution

Ticket Status distribution

Unresolved vs Resolved (Backlog)

Resolution Category distribution

Resolution Time summary

Priority vs Resolution Time (Boxplot)

Ticket Type vs Resolution Time (Boxplot)

Insights Extracted:

Ticket workload balanced across 5 major issue categories

Priority levels evenly distributed (Medium ≈ Critical ≈ High ≈ Low)

Mean resolution time ≈ 11.7 hours for closed tickets

SLA breach ≈ 0% for resolved tickets (24h SLA benchmark)

Major inefficiency ≈ 67% unresolved backlog

Slow resolution category dominated due to unresolved tickets

Outcome:
Module-3 converted raw dataset into actionable operational insights and performance KPIs needed for optimization.

# Module 4 — Optimization & Clustering (Week-4)

Objective:
To use insights from Module-3 to identify root causes of performance bottlenecks and propose optimization strategies using SLA analysis, clustering, and workload patterns.

Key Work Done:

Mapped bottlenecks to root causes

Performed SLA-based evaluation on resolution performance

Proposed optimization strategies for:

SLA prioritization

Ticket routing based on issue type

Customer follow-up automation

Agent load balancing

Knowledge base/self-service

Implemented clustering using Ticket Subject + Description fields

Calculated cluster sizes

Mapped clusters to dominant Ticket Types and Priority

Identified repetitive issue patterns for automation/FAQ candidates

Clustering Approach:

Vectorization: TF-IDF

Algorithm: KMeans (k=5)

Outputs:

Cluster size distribution

Dominant issue type per cluster

Dominant priority per cluster

Optimization Insights Extracted:

Large clusters indicate repetitive issue types

Technical & Refund clusters are ideal for automation

Billing & Product Inquiry clusters suitable for self-service knowledge base

Pending/Unresolved tickets require follow-up automation workflows

Outcome:
Module-4 translated EDA insights into practical optimization strategies to reduce backlog, improve resolution coverage, and enhance support performance.

# Milestone 3 – Module 5 & Module 6

# Module 5 – Performance Analytics

Work Completed

Created new column Resolution Time (Hours)

Calculated average resolution time

For entire dataset

By Ticket Type

By Priority

Mapped ticket types into Request / Incident / Problem

Analyzed high-priority tickets separately

Identified unresolved tickets

Performed trend analysis over time (monthly)

Visualizations Created

Bar chart: Ticket Type vs Average Resolution Time

Bar chart: Priority vs Average Resolution Time

Box plot: Ticket Category vs Resolution Time

Bar chart: High-Priority Ticket Category vs Resolution

Bar chart: Unresolved tickets by Priority

Line chart: Resolution time trend over time

Outcome

Identified performance differences by priority and ticket type

Found unresolved backlog as key challenge

Highlighted high-priority delay patterns

# Module 6 – Geographic & Cluster Analysis

Work Completed

Created a realistic Country column for geographic analysis

Calculated ticket volume by country

Compared resolution performance across countries

Performed text clustering on ticket descriptions

Calculated

Cluster size

Average resolution time per cluster

Analyzed relationship between cluster size and performance

Identified dominant issue type in each cluster

Visualizations Created

Bar chart & heatmap: Ticket concentration by country

Bar chart: Country vs Average Resolution Time

Scatter plot: Cluster Size vs Performance

Bar chart: Cluster vs Average Resolution Time

Outcome

Detected regions with slower performance

Identified repetitive issue clusters

Suggested automation and routing improvements
