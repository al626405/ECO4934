import pandas as pd

# Define file paths
ids_file = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/Filter-Sorted/filtered_ids.csv'
product_file = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/product.csv'
output_file = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/Filter-Sorted/filtered_product.csv'

# Load CSV files into pandas dataframes
df_ids = pd.read_csv(ids_file, header=None, names=['Key1'])  # Assuming no headers in filtered_ids.csv
df_product = pd.read_csv(product_file, header=None)  # Assuming no headers in product.csv

# Extract the IDs from the first column of filtered_ids.csv
ids = df_ids['Key1'].tolist()

# Filter rows in product.csv based on IDs from filtered_ids.csv
filtered_product = df_product[df_product.iloc[:, 0].isin(ids)]

# Drop duplicates based on the entire row
filtered_product = filtered_product.drop_duplicates()

# Save the filtered data to a new CSV file
filtered_product.to_csv(output_file, index=False, header=False)

print(f"Filtered product data (with duplicates removed) saved to {output_file}")

import pandas as pd

# Define file paths
input_file = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/Filter-Sorted/filtered_product.csv'
output_file = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/Filter-Sorted/Filtered/what_filtered_product.csv'

# Load the CSV file into a pandas dataframe
df = pd.read_csv(input_file, header=None)  # Assuming no headers

# Extract the 2nd column (index 1)
second_column = df.iloc[:, 1]

# Save the extracted column to a new CSV file
second_column.to_csv(output_file, index=False, header=False)

print(f"Second column of {input_file} saved to {output_file}")
