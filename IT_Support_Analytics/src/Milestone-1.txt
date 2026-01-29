import pandas as pd


print("Loading raw CSV file...")
df = pd.read_csv("../data/Data_2.csv", header=None)
print("Raw file loaded. Shape:", df.shape)
print(df.head(), "\n")

print("Splitting data into columns...")
df = df[0].str.split(",", expand=True)
print("Split completed. New shape:", df.shape)
print(df.head(), "\n")

print("Assigning column names...")
df.columns = [
    "Ticket_ID", "Type", "Category", "Priority",
    "Created_Date", "Resolution_Date", "Assigned_To", "Description"
]
print("Column names assigned.\n")

print("Checking missing values...")
print(df.isnull().sum(), "\n")

print("Normalizing priority values...")
priority_cleanup = {
    'low': 'Low', 'Low': 'Low',
    'medium': 'Medium', 'Medium': 'Medium',
    'high': 'High', 'High': 'High',
    'urgent': 'Critical', 'URGENT': 'Critical',
    'critical': 'Critical', 'Critical': 'Critical'
}
df['Priority'] = df['Priority'].replace(priority_cleanup)
print("Priority normalization completed.")
print(df['Priority'].value_counts(), "\n")

print("Filling missing text fields...")
text_cols = ['Type', 'Priority', 'Category', 'Assigned_To', 'Description']
for col in text_cols:
    df[col] = df[col].fillna("Unknown")
print("Missing text fields filled.\n")

print("Converting date columns...")
df['Created_Date'] = pd.to_datetime(df['Created_Date'], errors='coerce')
df['Resolution_Date'] = df['Resolution_Date'].replace("not_resolved", pd.NaT)
df['Resolution_Date'] = pd.to_datetime(df['Resolution_Date'], errors='coerce')
print("Date conversion completed.\n")

print("Calculating resolution duration...")
df['Resolution_Duration'] = (
    df['Resolution_Date'] - df['Created_Date']
).dt.total_seconds() / 3600
df['Resolution_Duration'] = df['Resolution_Duration'].fillna(-1)
print("Resolution duration calculated.\n")

print("Mapping priority scores...")
priority_map = {'Low': 1, 'Medium': 2, 'High': 3, 'Critical': 4}
df['Priority_Score'] = df['Priority'].map(priority_map)
print("Priority scores added.\n")

print("Saving cleaned dataset...")
output_path = "../data/Cleaned_Data_2.csv"
df.to_csv(output_path, index=False)
print("Cleaned dataset saved successfully at:", output_path)

print("Process completed successfully!")
