import pandas as pd

# Load dataset
df = pd.read_csv("../data/IT_Support_Tickets.csv")

# Basic exploration
print("Dataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nTicket Distribution by Type:")
print(df['Type'].value_counts())

print("\nTicket Distribution by Priority:")
print(df['Priority'].value_counts())

print("\nTicket Distribution by Category:")
print(df['Category'].value_counts())

# Handle missing text fields
text_columns = ['Type', 'Priority', 'Category', 'Country']
for col in text_columns:
    if col in df.columns:
        df[col] = df[col].fillna('Unknown')

# Convert date columns
df['Created_Date'] = pd.to_datetime(df['Created_Date'], errors='coerce')
df['Resolution_Date'] = pd.to_datetime(df['Resolution_Date'], errors='coerce')

# Feature: Resolution Duration (hours)
df['Resolution_Duration'] = (
    df['Resolution_Date'] - df['Created_Date']
).dt.total_seconds() / 3600

# Feature: Priority Score
priority_map = {
    'Low': 1,
    'Medium': 2,
    'High': 3,
    'Critical': 4
}
df['Priority_Score'] = df['Priority'].map(priority_map).fillna(0)

# Remove invalid records
df = df[df['Resolution_Duration'] >= 0]

# Save cleaned dataset
df.to_csv("../data/cleaned_it_support_tickets.csv", index=False)
