# 📊 Supportlytics – Milestone 1  
## Optimizing IT Support Team Performance Using Analytics

## Objective
1. To understand the structure, attributes, and quality of the IT support ticket dataset.

2. To analyze the distribution of support tickets based on type, priority, and issue category.

3. To evaluate IT support performance using time-based metrics such as resolution duration.

4. To transform raw ticket attributes into meaningful numerical features for analysis.

5. To prepare a clean, consistent, and analysis-ready dataset for further performance evaluation.

---

## key performance indicators (KPIs)

Average Resolution Duration (Hours) – Measures efficiency of ticket resolution.

Ticket Volume by Priority Level – Indicates workload distribution by urgency.

Ticket Distribution by Type – Shows the nature of support requests handled.

Customer Satisfaction Score – Reflects quality of support service delivered.

Category-wise Ticket Frequency – Identifies frequently occurring issue types.

---

## 📁 Folder Structure 
```
Saktheshwaran T - Milestone1/
│
├── SUPPORTLYTICS(M1).ipynb          # Milestone 1 analysis notebook
├── supportlytics_cleaned (1).csv   # Cleaned dataset
├── Corr.png                        # Correlation matrix
├── Distplot1.png                   # Ticket distribution by type
├── distplot2.png                   # Ticket distribution by priority
├── distplot3.png                   # Top issue categories
└── readme.md                       # Milestone 1 documentation
```

---

## Data Analysis

### 🔹 Correlation Analysis
- Generated correlation matrix for numerical features
- Observed weak correlations indicating independent variables

**File:** Corr.png

---

### 🔹 Ticket Distribution by Type
- Analyzed frequency of ticket types

**File:** Distplot1.png

---

### 🔹 Ticket Distribution by Priority
- Visualized tickets across priority levels

**File:** distplot2.png

---

### 🔹 Top Issue Categories
- Identified most frequent issue categories

**File:** distplot3.png

---

## 🛠 Tools & Technologies
- Python
- Pandas
- Matplotlib
- Seaborn
- Colab Notebook

---
# Feature Engineering Summary

Resolution duration was engineered by calculating the time difference between first response and resolution timestamps and converting it into hours.

Ticket priority was transformed into a numerical priority score using ordinal encoding.

Missing numerical values were handled using median-based central tendency imputation.

Categorical attributes were cleaned and standardized to ensure consistency.

Priority score and customer satisfaction rating were scaled to improve interpretability and comparison.

---

## Outcome
- Dataset cleaned and prepared
- Key insights extracted through EDA
- Ready for advanced analytics in future milestones

---



