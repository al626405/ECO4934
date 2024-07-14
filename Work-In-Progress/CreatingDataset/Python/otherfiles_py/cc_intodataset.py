import pandas as pd

# Step 1: Read the existing dataset
dataset = pd.read_csv('/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/Filter-Sorted/columns/Dataset.csv')

# Step 2: Read the cc updates from the CSV file
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

# Step 5: Save the merged dataset to a new CSV file
combined_dataset.to_csv('/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/combined_dataset.csv', index=False)

print("Combined dataset has been saved to 'combined_dataset.csv'")
