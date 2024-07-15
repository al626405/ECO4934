import pandas as pd

# Load the CSV files into DataFrames
sorted_cleaned_resolution_df = pd.read_csv("/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/Filter-Sorted/sorted_cleaned_reports.csv")
final_df = pd.read_csv("/home/Alexis/Database/Python/calculatedstatistics/Q1_dataset.csv")

# Standardize column names if needed
sorted_cleaned_resolution_df.rename(columns={'who': 'assigned_who'}, inplace=True)  # Rename 'who' to 'assigned_who'

# Calculate total reports for each assigned_who
total_reports = final_df['assigned_who'].value_counts().reset_index()
total_reports.columns = ['assigned_who', 'total_reports']

# Merge sorted_cleaned_resolution_df with final_df using report_id and assigned_who as primary key
merged_df = pd.merge(final_df, sorted_cleaned_resolution_df[['report_id', 'assigned_who', 'current_resolution', 'current_status']], 
                     left_on=['report_id', 'assigned_who'], right_on=['report_id', 'assigned_who'], how='left')

# Filter for cases where edits result in a bug being fixed
bug_edits_influence = merged_df[(merged_df['resolution'] == 'FIXED') & 
                                ((merged_df['bug_status'] == 'resolved') | (merged_df['bug_status'] == 'verified'))]

# Group by assigned_who and analyze influence of bug_status edits
bug_status_edits = bug_edits_influence.groupby('assigned_who').size().reset_index(name='bug_status_edits')

# Group by assigned_who and analyze influence of resolution edits
resolution_edits = bug_edits_influence.groupby('assigned_who').size().reset_index(name='resolution_edits')

# Create a DataFrame with all assigned_who from final_df
all_editors = pd.DataFrame(final_df['assigned_who'].unique(), columns=['assigned_who'])

# Merge with bug_status_edits
edits_influence = pd.merge(all_editors, bug_status_edits, on='assigned_who', how='left')
edits_influence['bug_status_edits'].fillna(0, inplace=True)

# Merge with resolution_edits
edits_influence = pd.merge(edits_influence, resolution_edits, on='assigned_who', how='left')
edits_influence['resolution_edits'].fillna(0, inplace=True)

# Calculate fixed bugs influenced by each editor
fixed_bugs_by_editor = bug_edits_influence.groupby('assigned_who').size().reset_index(name='fixed_bugs')

# Merge with edits_influence to include fixed bugs counts
edits_influence = pd.merge(edits_influence, fixed_bugs_by_editor, on='assigned_who', how='left')
edits_influence['fixed_bugs'].fillna(0, inplace=True)

edits_influence['fixed_bugs'] = edits_influence['fixed_bugs'].astype(int)

# Merge with total_reports to include total report counts
edits_influence = pd.merge(edits_influence, total_reports, on='assigned_who', how='left')

# Calculate fixed_bugs / total_reports
edits_influence['fixed_bugs_ratio'] = edits_influence['fixed_bugs'] / edits_influence['total_reports']

# Drop unnecessary columns
edits_influence.drop(['bug_status_edits', 'resolution_edits'], axis=1, inplace=True)

# Sort by assigned_who in ascending order
edits_influence.sort_values(by='assigned_who', inplace=True)

# Save or further analyze the edits_influence DataFrame
edits_influence.to_csv('/home/Alexis/Database/Python/calculatedstatistics/Q3.csv', index=False)
