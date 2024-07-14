import csv
import os

# Define the path to the CSV files
csv_path = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/Filter-Sorted/Filtered/'

# List of CSV files to process
csv_files = [
    'id.csv', 'reportcol2.csv', 'reportcol3.csv', 'what_filtered_priority.csv', 
    'what_filtered_product.csv', 'what_filtered_version.csv', 
    'what_filtered_op_sys.csv', 'what_filtered_component.csv', 'what_filtered_severity.csv', 
    'when.csv', 'who.csv'
]

# List to store data from each CSV file
data = []

# Read each CSV file and store its data
for csv_file in csv_files:
    file_path = os.path.join(csv_path, csv_file)
    with open(file_path, 'r', newline='') as f:
        reader = csv.reader(f)
        data.append(list(reader))

# Assuming id.csv is the reference file, determine the maximum number of rows
max_rows = len(data[0])

# Check that all files have the same number of rows
for csv_data in data:
    if len(csv_data) != max_rows:
        raise ValueError("CSV files have different number of rows. Please ensure they are consistent.")

# Write combined data to a new CSV file
output_file = os.path.join(csv_path, 'combined_dataset.csv')
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)

    # Write headers if needed
    headers = next(iter(data))
    writer.writerow(headers[0])

    # Write data
    for row in zip(*data):
        combined_row = []
        for item in row:
            combined_row.extend(item)
        writer.writerow(combined_row)

print("CSV files concatenated successfully into combined_dataset.csv.")
