import pandas as pd

# Load the CSV files into DataFrames
bug_status_df = pd.read_csv("/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv/bug_status.csv")
assigned_to_df = pd.read_csv("/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv/assigned_to.csv")
resolution_df = pd.read_csv("/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv/resolution.csv")

# Merge the DataFrames based on 'report_id' and 'assigned_who' with 'bug_who' and 'res_who'
merged_df = pd.merge(assigned_to_df, bug_status_df, left_on=['report_id', 'assigned_who'], right_on=['report_id', 'bug_who'], suffixes=('_assigned', '_bug'))
merged_df = pd.merge(merged_df, resolution_df, left_on=['report_id', 'assigned_who'], right_on=['report_id', 'res_who'])

# Rename columns to make them more readable or distinct
merged_df.columns = [
    'id_assigned', 'report_id', 'assigned_to', 'assigned_when', 'assigned_who',
    'id_bug', 'bug_status', 'bug_when', 'bug_who',
    'id_resolution', 'resolution', 'res_when', 'res_who'
]

# Remove unnecessary columns
merged_df = merged_df.drop(columns=['id_bug', 'id_resolution', 'bug_who', 'res_who'])

# Filter out rows where 'assigned_to' is 'None'
filtered_df = merged_df[merged_df['assigned_to'] != 'None']

# Select relevant columns
final_df = filtered_df[['id_assigned', 'report_id', 'assigned_who', 'assigned_to', 'assigned_when', 'bug_status', 'bug_when', 'resolution', 'res_when']]

# Save the resulting DataFrame to a new CSV file
final_df.to_csv("/home/Alexis/Database/Python/calculatedstatistics/Q1_dataset1.csv", index=False)

print("Final dataset saved successfully.")
