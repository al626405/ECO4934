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
