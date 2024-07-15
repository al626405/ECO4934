import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("/home/Alexis/Database/Python/calculatedstatistics/Q1_dataset.csv")

# Filter out rows where `what_assigned_to` is 'None'
df_filtered = df[df['assigned_to'] != 'None']

# Calculate the success rate of each bug assignee
# A success is defined as having a resolution of 'FIXED'
success_df = df_filtered[df_filtered['resolution'] == 'FIXED']
success_counts = success_df.groupby('assigned_to').size().reset_index(name='fixed_count')

# Count the total number of assignments for each assignee
total_counts = df_filtered.groupby('assigned_to').size().reset_index(name='total_count')

# Merge the success counts with the total counts to calculate the success rate
assignee_stats = pd.merge(success_counts, total_counts, on='assigned_to')
assignee_stats['success_rate'] = assignee_stats['fixed_count'] / assignee_stats['total_count']

# Merge the success rate information back with the original filtered data
df_with_success_rate = pd.merge(df_filtered, assignee_stats[['assigned_to', 'success_rate']], on='assigned_to', how='left')

# Print the resulting DataFrame with the success rates
print(df_with_success_rate)

# Save the resulting DataFrame to a new CSV file
df_with_success_rate.to_csv("/home/Alexis/Database/Python/calculatedstatistics/Q1-Data_with_success_rate.csv", index=False)

print("Data with success rates saved successfully.")
