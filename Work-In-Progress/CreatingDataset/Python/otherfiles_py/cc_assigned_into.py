import pandas as pd

# Step 1: Read the existing dataset
dataset = pd.read_csv('/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/combine_test/Dataset.csv')

# Step 2: Read the cc updates from the CSV file (cc_cleaned.csv)
cc_updates = pd.read_csv('/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/cc_cleaned.csv')

# Step 3: Aggregate the cc updates by report_id
cc_aggregated = cc_updates.groupby('report_id').agg({
    'cc_email': lambda x: '; '.join(x),
    'cc_when': lambda x: '; '.join(x.astype(str)),
    'cc_who': lambda x: '; '.join(x.astype(str))
}).reset_index()

# Step 4: Merge the aggregated cc updates into the existing dataset
combined_dataset = pd.merge(dataset, cc_aggregated, on='report_id', how='left')

# Fill missing values with 'None'
combined_dataset['cc_email'].fillna('None', inplace=True)
combined_dataset['cc_when'].fillna('None', inplace=True)
combined_dataset['cc_who'].fillna('None', inplace=True)

# Step 5: Read assigned_to updates from assigned_to.csv
assigned_to_updates = pd.read_csv('/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/assigned_to.csv')

# Step 6: Aggregate assigned_to updates by report_id
assigned_to_aggregated = assigned_to_updates.groupby('report_id').agg({
    'assigned_to': lambda x: '; '.join(x),
    'assigned_when': lambda x: '; '.join(x.astype(str)),
    'assigned_who': lambda x: '; '.join(x.astype(str))
}).reset_index()

# Step 7: Merge assigned_to aggregated updates into the combined dataset
combined_dataset = pd.merge(combined_dataset, assigned_to_aggregated, on='report_id', how='left')

# Fill missing values with 'None'
combined_dataset['assigned_to'].fillna('None', inplace=True)
combined_dataset['assigned_when'].fillna('None', inplace=True)
combined_dataset['assigned_who'].fillna('None', inplace=True)

# Step 8: Read resolution updates from resolution_cleaned.csv
resolution_updates = pd.read_csv('/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/resolution_cleaned.csv')

# Step 9: Aggregate resolution updates by report_id
resolution_aggregated = resolution_updates.groupby('report_id').agg({
    'resolution_update': lambda x: '; '.join(x),
    'resolution_when': lambda x: '; '.join(x.astype(str)),
    'resolution_who': lambda x: '; '.join(x.astype(str))
}).reset_index()

# Step 10: Merge resolution aggregated updates into the combined dataset
combined_dataset = pd.merge(combined_dataset, resolution_aggregated, on='report_id', how='left')

# Fill missing values with 'None'
combined_dataset['resolution_update'].fillna('None', inplace=True)
combined_dataset['resolution_when'].fillna('None', inplace=True)
combined_dataset['resolution_who'].fillna('None', inplace=True)

# Step 11: Read bug_status updates from bug_status_cleaned.csv
bug_status_updates = pd.read_csv('/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/bug_status_final.csv')

# Step 12: Aggregate bug_status updates by report_id
bug_status_aggregated = bug_status_updates.groupby('report_id').agg({
    'bug_status_update': lambda x: '; '.join(x),
    'bug_status_when': lambda x: '; '.join(x.astype(str)),
    'bug_status_who': lambda x: '; '.join(x.astype(str))
}).reset_index()

# Step 13: Merge bug_status aggregated updates into the combined dataset
combined_dataset = pd.merge(combined_dataset, bug_status_aggregated, on='report_id', how='left')

# Fill missing values with 'None'
combined_dataset['bug_status_update'].fillna('None', inplace=True)
combined_dataset['bug_status_when'].fillna('None', inplace=True)
combined_dataset['bug_status_who'].fillna('None', inplace=True)

# Step 14: Save the merged dataset to a new CSV file
combined_dataset.to_csv('/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/combine_test/combined_dataset.csv', index=False)

print("Combined dataset has been saved to 'combined_dataset.csv'")
