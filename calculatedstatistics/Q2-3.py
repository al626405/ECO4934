import pandas as pd

# Load the CSV files into DataFrames
sorted_cleaned_resolution_df = pd.read_csv("/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/Filter-Sorted/sorted_cleaned_reports.csv")
final_df = pd.read_csv("/home/Alexis/Database/Python/calculatedstatistics/Q1_dataset.csv")

# Standardize column names if needed
sorted_cleaned_resolution_df.rename(columns={'who': 'assigned_who'}, inplace=True)  # Assuming 'who' in sorted_cleaned_resolution.csv corresponds to 'assigned_who' in final_df

# Merge sorted_cleaned_resolution_df with final_df using report_id and assigned_who as primary key
merged_df = pd.merge(final_df, sorted_cleaned_resolution_df[['report_id', 'assigned_who', 'current_resolution', 'current_status']], 
                     left_on=['report_id', 'assigned_who'], right_on=['report_id', 'assigned_who'], how='left')

# Calculate the is_fixed column based on current_resolution
merged_df['is_fixed'] = merged_df['current_resolution'].apply(lambda x: 1 if x == 'FIXED' else 0)

# Calculate total reports for each assigned_who
total_reports = merged_df.groupby('assigned_who').size().reset_index(name='total_reports')

# Calculate fixed reports (success rate) for each assigned_who
fixed_reports = merged_df[merged_df['is_fixed'] == 1].groupby('assigned_who').size().reset_index(name='fixed_reports')

# Merge total_reports and fixed_reports to calculate reputation
bug_reporters_reputation = pd.merge(total_reports, fixed_reports, on='assigned_who', how='left')

# Fill NaN values with 0 for 'fixed_reports'
bug_reporters_reputation['fixed_reports'].fillna(0, inplace=True)

# Calculate reputation (fixed_reports / total_reports)
bug_reporters_reputation['reputation'] = bug_reporters_reputation['fixed_reports'] / bug_reporters_reputation['total_reports']

# Fill NaN values in 'reputation' with 0 (for cases where total_reports might be 0)
bug_reporters_reputation['reputation'].fillna(0, inplace=True)

# Save to CSV or further process bug_reporters_reputation DataFrame
bug_reporters_reputation.to_csv('/home/Alexis/Database/Python/calculatedstatistics/Q2-test.csv', index=False)

# Print or further analyze bug_reporters_reputation DataFrame
print(bug_reporters_reputation)

# Group by report_id and assigned_who to count reports per reporter per report_id
reports_per_reporter = final_df.groupby(['report_id', 'assigned_who']).size().reset_index(name='edits')

# Sort by report_id (lowest to greatest)
reports_per_reporter.sort_values(by='assigned_who', inplace=True)

# Save or further analyze reports_per_reporter DataFrame
reports_per_reporter.to_csv('/home/Alexis/Database/Python/calculatedstatistics/Q3-test.csv', index=False)
print(reports_per_reporter)
