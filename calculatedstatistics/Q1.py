import pandas as pd

# Load the CSV files into DataFrames
bug_status_df = pd.read_csv("/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv/bug_status.csv")
assigned_to_df = pd.read_csv("/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv/assigned_to.csv")
resolution_df = pd.read_csv("/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv/resolution.csv")

# Merge the DataFrames based on 'report_id' and 'who'
merged_df = pd.merge(bug_status_df, assigned_to_df, on=['report_id', 'who'], suffixes=('_bug_status', '_assigned_to'))
merged_df = pd.merge(merged_df, resolution_df, on=['report_id', 'who'])

# Optionally, you can rename columns to make them more readable or distinct
merged_df.columns = [
    'id_bug_status', 'report_id', 'what_bug_status', 'when_bug_status', 'who',
    'id_assigned_to', 'what_assigned_to', 'when_assigned_to',
    'id_resolution', 'what_resolution', 'when_resolution'
]
merged_df = merged_df.drop(columns=['id_bug_status', 'id_assigned_to', 'id_resolution'])
# Save the resulting DataFrame to a new CSV file
merged_df.to_csv("/home/Alexis/Database/Python/calculatedstatistics/Q1-Data.csv", index=False)

print("Merged file saved successfully.")
