import pandas as pd

# Load the CSV files into DataFrames
final_df = pd.read_csv("/home/Alexis/Database/Python/calculatedstatistics/Q1_dataset.csv")
sorted_cleaned_resolution_df = pd.read_csv("/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/Filter-Sorted/sorted_cleaned_reports.csv")

# Merge final_df with sorted_cleaned_resolution_df on report_id and assigned_who (who in sorted_cleaned_resolution_df)
merged_df = pd.merge(final_df, sorted_cleaned_resolution_df[['report_id', 'who', 'current_resolution']], 
                     left_on=['report_id', 'assigned_who'], right_on=['report_id', 'who'], how='left')

# Count all bug_status edits per reporter
bug_status_edits = merged_df.groupby('assigned_who')['bug_status'].apply(lambda x: x.notna().sum()).reset_index(name='bug_status_total_edits')

# Count all resolution edits per reporter
resolution_edits = merged_df.groupby('assigned_who')['resolution'].apply(lambda x: x.notna().sum()).reset_index(name='resolution_total_edits')

bug_status_edits_influence = merged_df[(merged_df['bug_status'] == 'resolved') | (merged_df['bug_status'] == 'verified')]

# Count bug_status edits that lead to a bug being fixed per reporter
bug_status_edits_count = bug_status_edits_influence.groupby('assigned_who').size().reset_index(name='bug_status_edits_fixed')

# Similarly, count resolution edits that lead to a bug being fixed per reporter
resolution_edits_influence = merged_df[merged_df['resolution'] == 'FIXED']
resolution_edits_count = resolution_edits_influence.groupby('assigned_who').size().reset_index(name='resolution_edits_fixed')

edits_counts = pd.merge(bug_status_edits, bug_status_edits_count, on='assigned_who', how='outer').fillna(0)
edits_counts = pd.merge(edits_counts, resolution_edits, on='assigned_who', how='outer').fillna(0)
edits_counts = pd.merge(edits_counts, resolution_edits_count, on='assigned_who', how='outer').fillna(0)

# Save or further analyze edits_counts DataFrame
edits_counts.to_csv('/home/Alexis/Database/Python/calculatedstatistics/edits_counts.csv', index=False)

# Print or further analyze edits_counts DataFrame
print(edits_counts)
