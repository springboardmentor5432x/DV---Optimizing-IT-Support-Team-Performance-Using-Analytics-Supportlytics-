**Supportlytics: Optimizing IT Support Performance through Data Analytics**

**Executive Summary**

This project focuses on enhancing the efficiency of an IT Support department by analyzing ticket lifecycles. By processing a dataset of support interactions, I established a baseline Average Resolution Time of 33.24 hours. Through data cleaning, feature engineering, and cluster analysis, I identified that administrative topics like "Training" and "Licensing" are significant bottlenecks. The project culminates in a Power BI dashboard designed to provide real-time visibility into support health.

**Business Problem Statement**

The support team faced challenges in meeting SLAs due to a lack of visibility into which ticket types consumed the most resources. Without a structured way to measure "Resolution Duration" or segment ticket performance, it was impossible to identify if delays were caused by technical complexity, high ticket volume, or specific departmental inefficiencies.

**Milestone 1 – Data Understanding & Exploratory Analysis**

**Objective:**
To perform an initial assessment of the support ticket data and identify key variables for performance tracking.

**Activities Performed:**

Loaded the Technical Support Dataset.csv.

Conducted data profiling and identified missing values in the "Status" and "Priority" columns.

**Key Decision:**
Defined Resolution_Duration as the primary target metric for the study to quantify operational lag.

**Milestone 2 – Data Cleaning & Feature Engineering**

**Objective:** 
To prepare a high-quality dataset and create meaningful metrics for deeper analysis.

**Data Preprocessing Steps:**

Standardized categorical labels and handled date-time conversions.

**Feature Engineering:**

**Resolution_Duration:** Calculated hours elapsed from "Open" to "Closed" status.

**Performance_Bucket:** Segmented tickets into "Efficient," "Average," and "Slow" based on the 33.24h mean.

**Milestone 3 – Clustering & Analytical Modeling**

**Objective:** 
To segment support tickets into logical groups to identify hidden patterns in resolution efficiency.

**Methodology:** Utilized grouping and aggregation to create a Cluster Performance Summary.

**Key Insight:** Discovered that Training Requests (38.89h) take significantly longer than Bug Reports (29.91h), indicating that non-technical queries are currently the biggest drag on team resources.

**Milestone 4 – Dashboard Development & Business Intelligence**

**Objective:**
To transform the analyzed data into an interactive visual interface using Power BI.

**Dashboard Design Principles:**

**Clarity:** Used high-contrast visuals to separate ticket priorities.

**Interactivity:** Integrated slicers for "Topic" and "Priority" to allow department-specific deep dives.

**Dashboard Structure:**

**Top Layer:** KPI cards for total volume and average resolution speed.

**Middle Layer:** Distribution charts (Tickets by Category).

**Bottom Layer:** Efficiency heatmaps and regional comparisons.

**Key Performance Indicators (KPIs):**

**Average Resolution Time (ART):** 33.24 hours.

**Total Ticket Volume:** Total count of active vs. resolved tickets.

**High-Priority Volume:** Real-time count of critical issues requiring immediate attention.

**Core Visualizations & Interpretation**

**Tickets by Priority & Type:**
A count plot showing that 'Medium' priority tickets form the bulk of the workload, but 'High' priority tickets in certain categories face disproportionate delays.

**Department Efficiency Analysis (Volume vs. Resolution Time):**
A scatter plot identifying departments that are "Overloaded" (High Volume, High Resolution Time).

**Cluster Performance – Volume vs. Resolution Time:**
This visual highlights the 9-hour efficiency gap between technical fixes and administrative requests.

**Key Insights**

**The "Training" Gap:** 
Training requests are the slowest category (38.89h), representing a major opportunity for "Shift-Left" strategies (self-service).

**Technical Efficiency:** 
"Bug Reports" are handled most efficiently (29.91h), suggesting the technical staff is well-trained, but the administrative process is lagging.

**Priority Misalignment:** 
High-priority tickets often take as long as low-priority ones in the "Licensing" category, indicating a process bottleneck regardless of urgency.

**Tools & Technologies Used**

**Data Processing:** Python (Pandas, NumPy).

**Visualization:** Matplotlib, Seaborn.

**Business Intelligence:** Power BI (Dasboard_Infosys.pbix).

**Business Impact**

**Resource Optimization:** Identified the need to reallocate staff from technical "Bug" teams to "Administrative/Licensing" queues.

**Strategic Savings:** Implementing a Knowledge Base for Training could reduce overall resolution time by 12%.

**Real-time Monitoring:** The dashboard allows managers to see spike patterns before they become backlogs.

**Conclusion**

The Supportlytics analysis proves that resolution speed is heavily influenced by the topic of the request. By using the developed Power BI dashboard to monitor the "Training" and "Licensing" clusters, the IT support team can implement targeted interventions to improve their overall efficiency and user satisfaction scores.
