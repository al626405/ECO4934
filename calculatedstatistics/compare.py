import pandas as pd

# Load the CSV files into DataFrames
q1_test_df = pd.read_csv("/home/Alexis/Database/Python/calculatedstatistics/Q1_TEST.csv")
q1_data_with_success_rate_df = pd.read_csv("/home/Alexis/Database/Python/calculatedstatistics/Q1-Data_with_success_rate.csv")

# Define key columns for comparison
key_columns = ['id_assigned', 'report_id', 'assigned_who', 'assigned_to', 'assigned_when', 'bug_status', 'bug_when', 'resolution', 'res_when']

# Merge DataFrames on key columns
comparison_df = pd.merge(q1_test_df, q1_data_with_success_rate_df, on=key_columns, suffixes=('_test', '_data_with_success_rate'), how='outer', indicator=True)

# Identify discrepancies
rows_in_test_not_in_data = comparison_df[comparison_df['_merge'] == 'left_only']
rows_in_data_not_in_test = comparison_df[comparison_df['_merge'] == 'right_only']
rows_in_both = comparison_df[comparison_df['_merge'] == 'both']

# Drop the merge indicator column
comparison_df = comparison_df.drop(columns=['_merge'])

# Save the comparison results to CSV files for further inspection
rows_in_test_not_in_data.to_csv("/home/Alexis/Database/Python/calculatedstatistics/rows_in_test_not_in_data.csv", index=False)
rows_in_data_not_in_test.to_csv("/home/Alexis/Database/Python/calculatedstatistics/rows_in_data_not_in_test.csv", index=False)
rows_in_both.to_csv("/home/Alexis/Database/Python/calculatedstatistics/rows_in_both.csv", index=False)

# Print summary statistics
print("Comparison completed.")
print(f"Rows in Q1_TEST.csv but not in Q1_dataset_with_success_rate.csv: {len(rows_in_test_not_in_data)}")
print(f"Rows in Q1_dataset_with_success_rate.csv but not in Q1_TEST.csv: {len(rows_in_data_not_in_test)}")
print(f"Rows in both CSV files: {len(rows_in_both)}")

# Additional Verification
# Load original data sources
bug_status_df = pd.read_csv("/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv/bug_status.csv")
assigned_to_df = pd.read_csv("/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv/assigned_to.csv")
resolution_df = pd.read_csv("/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv/resolution.csv")

# Verify success rates against original data
# Merge the DataFrames based on 'report_id' and 'assigned_who' with 'bug_who' and 'res_who'
merged_df = pd.merge(assigned_to_df, bug_status_df, left_on=['report_id', 'assigned_who'], right_on=['report_id', 'bug_who'], suffixes=('_assigned', '_bug'))
merged_df = pd.merge(merged_df, resolution_df, on=['report_id'], suffixes=('_assigned', '_resolution'))

# Calculate success rate from merged original data
filtered_df = merged_df[merged_df['assigned_to'] != 'None']
filtered_df = filtered_df[(filtered_df['resolution'] == 'FIXED') & (filtered_df['bug_status'].isin(['resolved', 'verified']))]

# Calculate success rate for each assigned_to
success_counts = filtered_df.groupby('assigned_to').size().reset_index(name='fixed_count')
total_counts = assigned_to_df.groupby('assigned_to').size().reset_index(name='total_count')
assignee_stats = pd.merge(success_counts, total_counts, on='assigned_to')
assignee_stats['success_rate'] = assignee_stats['fixed_count'] / assignee_stats['total_count']

# Merge success rate back to original merged DataFrame
merged_df = pd.merge(merged_df, assignee_stats[['assigned_to', 'success_rate']], on='assigned_to', how='left')

# Check for discrepancies in success rate calculations
discrepancies = merged_df[merged_df['success_rate'] != merged_df['success_rate']]

# Save discrepancies for inspection
discrepancies.to_csv("/home/Alexis/Database/Python/calculatedstatistics/discrepancies.csv", index=False)

print("Verification completed. Discrepancies saved to discrepancies.csv.")
