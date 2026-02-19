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
- [Exploratory Visualization & Similarity and Cluster Insights ] (notebooks/milestone 2.ipynb)

## 🛠 Tools & Technologies Used
- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Power BI (DAX, Data Modeling, Dashboard Design)
- Jupyter Notebook (Data Cleaning, Transformation & Analysis)
- KMeans Clustering (Scikit-learn)

## Dataset Description
The dataset contains:
- Ticket ID
- Created time
- First response time
- Closing time
- Resolution Duration (in hours)
- Status (Resolved, Closed, Open, New, In Progress)
- Priority (Low, Medium, High, Critical)
- Source
- Topic (Ticket Issue)
- Product group (Ticket Category)
- Country
- Latitude & Longitude
- Cluster ID (generated using KMeans)
- Survey results

### Data Preparation & Processing
#### 1. Data Cleaning
- Checked for missing values
- Removed unwanted columns
- Converted date columns to datetime format

 #### 2. Feature Engineering
- Added Resolution Duration(hours) column by subtracting Resolution time - Created time
- Added First Respone time(minutes) column by subtracting Resolution time - Created time
- Encoded Priority column into a numeric Priority Score column for clustering

### Exploratory Data Analysis (Python)
#### 1. Ticket Volume Analysis
- Count of tickets by category
- Count by Priority
- Count of tickets by ticket issue

#### 2. High-Priority Analysis

High + Critical ticket count

High-priority resolution time comparison

#### 3. Regional Performance

Average resolution time by region

Heatmap of ticket concentration

#### 4. Category Comparison

Ticket distribution by category and country

Category-wise performance comparison
