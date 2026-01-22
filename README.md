***Project:*** Supportlytics-Data-Driven Optimization of IT Support Team Performance

**Milestone 1: Data Preparation & Feature Engineering**


1. **Objective of Milestone 1**
The objective of this milestone is to prepare the dataset for analysis by performing data loading, exploration, cleaning, and feature engineering. This step ensures that the data is structured, reliable, and suitable for performance analytics in later milestones.

2. Dataset Description
**Dataset Name:** Customer Support Ticket Dataset  
**Source:** Kaggle  

The dataset contains real-world customer support ticket records, including ticket priority, status, response time, resolution time, and customer satisfaction ratings. These attributes allow meaningful analysis of IT support performance and efficiency.

3. Tools & Technologies Used
- Google Colab  
- Python  
- Pandas  
- NumPy  

4. Tasks Completed in Milestone 1

4.1 Data Loading & Understanding
- Loaded dataset into Google Colab
- Explored dataset structure, columns, and data types
- Identified missing values and inconsistent data formats

4.2 Data Cleaning
- Removed personally identifiable information (PII) such as:
  - Customer Name
  - Customer Email
  - Customer Age
  - Customer Gender
- Handled missing values using median imputation
- Converted timestamp fields to proper datetime format

4.3 Feature Engineering
The following new features were created to support performance analysis:
- Resolution_Duration_Hours 
  - Calculated using the difference between resolution time and first response time
- First_Response_Duration_Hours  
  - Converted response timestamps into numeric duration
- Resolution_Efficiency  
  - Derived using resolution duration and response duration
- Priority_Score  
  - Numerical mapping of ticket priority levels

5. Key Performance Indicators (KPIs)
- First Response Time
- Time to Resolution
- Resolution Duration (Hours)
- Resolution Efficiency
- Ticket Priority Distribution
- Ticket Status
- Customer Satisfaction Rating

6. Files in This Milestone
- `Milestone1_Data_Preparation.ipynb`  
  - Google Colab notebook containing all preprocessing and feature engineering steps  
- `cleaned_customer_support_tickets.csv`  
  - Cleaned and processed dataset ready for analysis  

7. Outcome of Milestone 1
At the end of this milestone:
- The dataset is clean, privacy-compliant, and analysis-ready
- All required KPIs and performance-related features are created
- The data is suitable for visualization, clustering, and performance optimization in upcoming milestones

8. Next Steps
- Exploratory Data Analysis (EDA)
- Visualization of ticket trends and performance metrics
- Cluster and similarity analysis
- Dashboard development

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Milestone 2: Exploratory Visualization & Similarity-Based Cluster Analysis  

---

## Milestone Overview

Milestone 2 focuses on analyzing IT support ticket data using visual analytics and clustering techniques.  
Building on the cleaned dataset from **Milestone 1**, this milestone aims to identify key ticket patterns, group similar issues, and uncover performance gaps related to resolution time and customer satisfaction.

Both Milestone 1 and Milestone 2 are maintained in a single notebook to ensure continuity and make the overall project flow easy to understand and explain.

---

## Module 3: Exploratory Visualization

### Objective
The objective of Module 3 is to explore the dataset visually in order to understand ticket distribution, workload patterns, and basic operational performance before applying clustering techniques.

### Work Performed
In this module, multiple visualizations were created to analyze different aspects of the ticket data:

- Ticket type distribution to understand the nature of incoming requests  
- Ticket priority distribution to analyze urgency levels  
- Ticket resolution status (resolved vs unresolved) to assess operational effectiveness  
- Ticket channel distribution (used as a proxy for queue) to understand how tickets are routed  
- Top ticket categories by frequency to identify recurring issues  
- Ticket distribution by priority and channel to analyze workload distribution  
- Average resolution time by ticket priority to evaluate prioritization efficiency  

### Key Insights
- Ticket volume is fairly distributed across different types and priorities.  
- A small number of ticket categories occur frequently and contribute significantly to overall workload.  
- Most tickets are successfully resolved, indicating stable support operations.  
- Higher-priority tickets generally have lower resolution times, showing effective prioritization.  

---

## Module 4: Similarity and Cluster Insights

### Objective
The objective of Module 4 is to group similar tickets into clusters and analyze how different issue groups perform in terms of resolution time and customer satisfaction.

### Cluster Formation
Ticket subject and ticket description were combined into a single text field to capture complete issue context.  
TF-IDF vectorization was used to convert textual data into numerical features, and KMeans clustering was applied to group similar tickets into clusters.

### Cluster Frequency and Interpretation
Cluster sizes were analyzed to identify frequently occurring issue groups.  
Sample ticket subjects from each cluster were reviewed to understand the general nature of issues represented by each cluster.

### Average Similarity Scores Within Clusters
Cosine similarity was used to calculate how closely each ticket matches its assigned cluster centroid.  
Average similarity scores were computed for each cluster to assess internal consistency.

**Insight:**  
Clusters with higher similarity scores represent well-defined and consistent issue groups, while clusters with lower similarity scores indicate mixed or diverse issues.

### Cluster Size vs Issue Type
Cluster size was compared with dominant ticket subjects to identify which issue types drive larger clusters.

**Insight:**  
High-frequency issue types often dominate larger clusters and represent strong candidates for automation or process improvement.

### Performance Gap Analysis
Performance gaps were visualized using boxplots and scatter plots:

- Resolution time by cluster  
- Customer satisfaction by cluster  
- Similarity score vs resolution time  
- Resolution time vs customer satisfaction  

**Key Observations:**  
- Clusters with lower similarity scores tend to have longer resolution times.  
- Longer resolution times are associated with lower customer satisfaction.  
- Certain clusters show higher variability, indicating inconsistent handling and performance gaps.  

---

## Conclusion

Milestone 2 successfully combined exploratory visualization and similarity-based clustering to uncover meaningful patterns in IT support ticket data. The analysis identified recurring issue groups, highlighted performance inefficiencies, and demonstrated how issue complexity affects resolution time and customer satisfaction. These insights provide a strong foundation for further performance optimization in subsequent milestones.
