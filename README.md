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
- 

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
Approach:
Filtered resolved tickets with clusters
Used **KMeans clustering** to group tickets based on:
- Resolution duration
- Priority Score
- Category encoded

Cluster Metrics Computed:
- Cluster Size (number of tickets)
- Resolution Time per cluster
- Cluster size(Workload) vs Performance measure

Other cluster based analysis:
- Average Similarity Score of each Cluster
- Cluster size vs ticket type
- PCA Visualization of Ticket Clusters
- Priority Distribution Across Clusters
