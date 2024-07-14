import pandas as pd

# Define file paths
ids_file = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/Filter-Sorted/filtered_ids.csv'
cc_file = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/cc_corrected.csv'
output_cc_file = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/Filter-Sorted/filtered_cc.csv'

# Load CSV files into pandas dataframes
df_ids = pd.read_csv(ids_file, header=None, names=['id'], dtype=str)  # Assuming no headers in filtered_ids.csv and convert to string
df_cc = pd.read_csv(cc_file, dtype=str)  # Assuming cc.csv has headers and convert to string

# Extract the IDs from the first column of filtered_ids.csv
ids = df_ids['id'].tolist()

# Filter rows in cc.csv based on IDs from filtered_ids.csv
filtered_cc = df_cc[df_cc.iloc[:, 0].isin(ids)]

# Save the filtered data to a new CSV file
filtered_cc.to_csv(output_cc_file, index=False)

print(f"Filtered cc data (with duplicates retained) saved to {output_cc_file}")
