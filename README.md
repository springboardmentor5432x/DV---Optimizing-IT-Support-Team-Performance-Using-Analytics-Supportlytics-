# DV - Optimizing IT Support Team Performance Using Analytics (Supportlytics)


## 📌 Project Overview
This project analyzes IT support ticket data to identify key performance trends, evaluate resolution times, and enhance operational efficiency through data analysis and visualization techniques. 

The goal is to uncover patterns in customer requests, technical issues, and support performance metrics to recommend improvements in workflow and resource allocation.

Using Python (EDA & clustering) and Power BI (interactive dashboard), the project identifies performance bottlenecks, severity impacts, and workload-performance relationships through tickets distribution across regions, categories, and priority levels.

## 📊 Key Objectives
- Understand and preprocess IT support ticket data for analysis
- Explore trends in ticket volume, priority, resolution time, and category distribution
- Identify clusters of similar issues using similarity scores and clustering techniques
- Evaluate high-priority and unresolved tickets handling
- Compare performance across regions and categories
- Visualize performance metrics through charts and interactive dashboard 
- Provide actionable insights for IT support optimization

## Dataset
Used a sythentic IT Service Management data from Kaggle
- [Raw Dataset](data/ITSM_Dataset.csv)
- [Cleaned Dataset](data/cleaned_ITSM_data.csv)
- [Clusters Dataset](data/ticket_clusters.csv)

## 📓 Notebooks
- [Data Preprocessing & Feature Engineering] (notebooks/milestone 1.ipynb)
- [EDA Visualizations, Similarity and Cluster Insights] (notebooks/milestone 2.ipynb)
- [Performance Analysis & Geographic, Category-level Insights] (notebooks/milestone 3.ipynb)

## 🛠 Tools & Technologies Used
- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Power BI (DAX, Data Modeling, Dashboard Design)
- Jupyter Notebook (Data Cleaning, Transformation & Analysis)
- KMeans Clustering (Scikit-learn)

## Dataset Description
The dataset contains:
- Ticket ID
- Created time
- First response time(in minutes)
- Closing time
- Resolution Duration (in hours)
- Status (Resolved, Closed, Open, New, In Progress)
- Priority (Low, Medium, High, Critical)
- Source
- Topic (Ticket Issue)
- Product group (Ticket Category)
- Country (Oman, Kuwait, Bahrain, UAE, Saudi Arabia, Qatar)
- Latitude & Longitude
- Cluster ID (generated using KMeans)
- Survey results
---

## Data Preparation & Processing
### 1. Data Cleaning
- Checked for missing values
- Removed unwanted columns
- Converted date columns to datetime format
- Filtered resolved tickets for performance metrics
- Created Date Table for Power BI time intelligence

 ### 2. Feature Engineering
- Added Resolution Duration(hours) column by subtracting Resolution time - Created time
- Added First Respone time(minutes) column by subtracting Resolution time - Created time
- Encoded Priority column into a numeric Priority Score column for clustering
- Resolved and unresolved tickets grouping separately
- Cluster ID assignment
- Created Similarity_Score indicating how closely each ticket matches the typical behaviour of its assigned cluster
- Created time-based attributes (Year, Month, Month no, YearMonth)


## Exploratory Data Analysis (Python)
### 1. Ticket Volume Analysis
- Ticket Distribution by its Issue types
- Ticket Distribution based on its Category
- Ticket Distribution based on its Priority
- Customer Satisfaction Distribution
- Ticket Distribution by its Source
- Unresolved tickets per priority 

### 2. High-Priority Analysis
- High + Critical ticket count
- Ticket Type vs Resolution Time comparison for higher priority tickets
- High-Priority Tickets Count by Category 

### 3. Ticket Resolution Analysis
- Total Average Resolution Time
- Computing Average Ticket Resolution times across issue types and priorities
- Resolved vs Resolving Tickets for its associated Agent Group
- Resolution time trend over time (Monthly and Weekly)

### 4. Regional Performance
- Average Resolution time across Countries
- Heatmap of ticket concentration by country
- Geo-scatter map of ticket categories

### 5. Category Comparison
- Ticket distribution by category and country
- Category-wise performance comparison across Countries

## Clustering Analysis

These insights can guide better resource allocation and targeted process improvements by identifying the clusters causing performance degradation.

Approach:
Filtered resolved tickets with clusters
Used **KMeans clustering** to group tickets based on:
- Resolution duration
- Priority Score
- Category encoded

Cluster Metrics Computed:
- Cluster Size (number of tickets)
- Resolution Time per cluster
- Cluster size(Workload) vs Avg Resolution time (Performance measure) scatter plot

Other cluster based analysis:
- Average Similarity Score of each Cluster: shows how internally consistent each cluster is
- Cluster size vs ticket type
- PCA Visualization of Ticket Clusters: illustrates cluster separation, overlap, and structural patterns, helping assess clustering effectiveness.
- Priority Distribution Across Clusters

### Cluster Insights
- Clusters 2 and 4 showed high workload and high resolution time → potential overload imbalance or repetitive issue patterns
- Clusters 3 and 5 maintained large volume but moderate performance → efficient handling
- Clusters 0 and 1 with high resolution time and less volume indicated complex issue types
- Since we find no clear trend, so workload(cluster size) is not the main driver (skill or category matters more).

## 📊 Power BI Dashboard Design
The final dashboard includes:

### 🔶 1. Problem Overview (KPI Section)
- Total Tickets
- Avg Resolution Time(hours)
- High Priority Tickets Count
- High Priority Tickets Avg Resolution Time(hours)
- Resolved tickets rate

### 🔶 2. Performance Analysis
- Ticket Volume by Category: Identifies dominant issue categories.
- High Priority Performance by Category: highlights risk areas.
- Ticket Resolution Status Distribution (Donut Chart): compares ticket resolution and backlogs
- Cluster Size vs Performance (Scatter Plot): shows workload impact across clusters
- Average Resolution Duration over Time(Months): describes resolution efficiency
- Regional Performance: Compares efficiency geographically.

### 🔶 3. Interactive Filters
The dashboard supports dynamic filtering by:
- Ticket Issue
- Priority
- Time Period
- Country

All visuals update instantly.

## 📌 Key Insights

- High & Critical tickets represent a significant percentage of total volume, indicating high operational pressure.
- Critical and Medium priority tickets have the largest backlog. This suggests that the critical marked tickets are getting stuck in the resolution process.
- Average Resolution time is 2.33 hours while High Priority tickets Average Resolution time is 1.33 hours describing that prioritzation policies are working efficiently.
- Resolved tickets rate is 40.15%.
- Certain countries and categories demonstrate higher average resolution time, suggesting resource or process inefficiencies.
- Specific categories like Hardware dominate ticket volume, requiring targeted expertise.
- Some clusters like 0 and 1 with lower ticket volume still show high resolution time, indicating complexity-driven delays.
- Cluster 2 and 4 shows highest workload and also elevated resolution time, while cluster 0 is taking long resolution time.
- Cluster 5 and 3 are best well defined and efficent.
- Access Request and Hardware Failure issue tickets require maximum resolution times.
- Upward trend observed in the average resolution time for the last few months(June, July, August) depicts increasing ticket complexity / workload over time.
- Qatar has highest ticket volume while Oman has longest ticket resolution durations.

## 🚀 Improvement Recommendations
🔹 1. Workload Redistribution
Balance tickets across clusters to prevent overload-driven delays.

🔹 2. Regional Resource Allocation
Increase staffing or automation in underperforming regions.

🔹 3. Category-Specific Training
Focus training on dominant or high-resolution-time categories.

🔹 4. Automation Opportunities
Automate frequently occurring low-complexity ticket categories.

🔹 5. Performance Monitoring Framework
Use dashboard for weekly performance reviews and SLA monitoring.

---

## 📈 Business Impact
This solution enables:
- Data-driven operational decisions
- Early detection of backlog or repitive risks
- SLA compliance monitoring
- Resource optimization
- Regional performance benchmarking
- Cluster-based workload analysis
---

## 🧠 Skills Demonstrated
- Data Cleaning & Transformation
- Exploratory Data Analysis
- Statistical Aggregation
- Clustering (KMeans)
- Performance Analytics
- DAX Measures
- Interactive Dashboard Design
- Business Insight Generation
***

## Conclusion

This project successfully integrates data analytics and business intelligence to evaluate IT support performance.

The interactive Power BI dashboard transforms raw ticket data into actionable insights, enabling continuous performance monitoring and operational optimization.

The combination of clustering and KPI analysis provides both macro-level and micro-level performance visibility.
