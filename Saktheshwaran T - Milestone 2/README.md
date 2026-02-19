# 📊 Supportlytics – Milestone 2  
## Exploratory Visualization & Cluster-Based Performance Insights  

---

## Objective

1. To perform detailed exploratory visualization of IT support ticket data.  
2. To analyze cluster behavior and similarity scores to identify recurring issue patterns.  
3. To evaluate performance gaps across clusters, priorities, and categories.  
4. To understand the relationship between cluster size, similarity score, and resolution efficiency.  
5. To generate meaningful visual insights that guide performance optimization strategies.

---

## Key Performance Indicators (KPIs)

- Average Similarity Score per Cluster – Measures how closely related issues are within a cluster.  
- Cluster-wise Average Resolution Duration – Identifies efficiency differences across issue groups.  
- Cluster Size (Ticket Count) – Highlights frequently occurring technical problems.  
- Priority-wise Resolution Distribution – Compares urgency handling performance.  
- Category-wise Cluster Concentration – Shows dominant issue types within clusters.

---

## 📁 Folder Structure

Saktheshwaran T - Milestone2/
│
├── SUPPORTLYTICS(M2).ipynb          # Milestone 2 analysis notebook
├── cluster_analysis_visuals/        # Saved visualizations
├── processed_dataset.csv            # Dataset used for clustering insights
└── readme.md                        # Milestone 2 documentation

---

## Data Analysis

### 🔹 Ticket Type Distribution
- Visualized distribution of Request, Incident, and Problem tickets.
- Identified dominant support request categories.

### 🔹 Top Clusters by Frequency
- Analyzed cluster size using ticket count.
- Identified recurring technical issue groups.

### 🔹 Similarity Score Analysis
- Calculated average similarity score within each cluster.
- Compared cluster cohesion levels.

### 🔹 Cluster Size vs Resolution Duration
- Used scatter plots to detect relationship between workload and performance.
- Identified clusters with high volume but slow resolution.

### 🔹 Priority vs Resolution Performance
- Compared average resolution time across priority levels.
- Highlighted performance gaps in high-priority tickets.

### 🔹 Boxplot Analysis of Cluster Performance
- Visualized resolution time spread within clusters.
- Detected outliers and inconsistent performance groups.

---

## 🛠 Tools & Technologies

- Python  
- Pandas  
- Matplotlib  
- Seaborn  
- Plotly  
- Colab Notebook  

---

# Cluster & Similarity Analysis Summary

Cluster performance was evaluated using ticket count, average similarity score, and average resolution duration.

High-similarity clusters indicate standardized recurring issues, suggesting potential for automation.

Low-similarity clusters represent diverse problem types requiring expert handling.

Resolution duration trends across clusters reveal operational bottlenecks.

Clusters with high priority concentration were analyzed separately to detect SLA risk areas.

---

