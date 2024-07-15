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
merged_df['is_fixed'] = merged_df['resolution'].apply(lambda x: 1 if x == 'FIXED' else 0)

# Filter for reporters who reported (total_reports)
# Condition: current_status is not 'resolved' or 'verified' and current_resolution is not 'FIXED'
bugs_reported = merged_df[(merged_df['current_status'] != 'resolved') & 
                          (merged_df['current_status'] != 'verified') & 
                          (merged_df['current_resolution'] != 'FIXED')].copy()

# Group by 'assigned_who' and count the total reports
total_reports = bugs_reported.groupby('assigned_who').size().reset_index(name='total_reports')

# Filter for reporters who fixed bugs (fixed_reports)
# Condition: current_resolution is 'FIXED' and current_status is 'resolved' or 'verified'
bugs_fixed = merged_df[(merged_df['resolution'] == 'FIXED') & 
                       ((merged_df['bug_status'] == 'resolved') | (merged_df['bug_status'] == 'verified'))].copy()

# Group by 'assigned_who' and count the fixed reports
fixed_reports = bugs_fixed.groupby('assigned_who').size().reset_index(name='fixed_reports')

# Merge total_reports and fixed_reports to calculate reputation
bug_reporters_reputation = pd.merge(total_reports, fixed_reports, on='assigned_who', how='left')

# Fill NaN values with 0 for 'fixed_reports' and 'total_reports'
bug_reporters_reputation['fixed_reports'].fillna(0, inplace=True)
bug_reporters_reputation['total_reports'].fillna(0, inplace=True)

# Convert 'fixed_reports' and 'total_reports' to integers
bug_reporters_reputation['fixed_reports'] = bug_reporters_reputation['fixed_reports'].astype(int)
bug_reporters_reputation['total_reports'] = bug_reporters_reputation['total_reports'].astype(int)

# Calculate reputation (fixed_reports / total_reports)
bug_reporters_reputation['reputation'] = bug_reporters_reputation['fixed_reports'] / bug_reporters_reputation['total_reports']

# Fill NaN values in 'reputation' with 0 (for cases where total_reports might be 0)
bug_reporters_reputation['reputation'].fillna(0, inplace=True)

# Save to CSV
bug_reporters_reputation.to_csv('/home/Alexis/Database/Python/calculatedstatistics/Q2_reputation.csv', index=False)

# Print or further process bug_reporters_reputation DataFrame
print(bug_reporters_reputation)
