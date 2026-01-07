**Optimizing IT Support Team Performance Using Analytics**

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
