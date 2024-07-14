import csv
import os

# Define the path to the CSV files
csv_path = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/Filter-Sorted/'

# List of what_* CSV files
what_files = [
    'what_sorted_cleaned_reports.csv', 'what_filtered_priority.csv',
    'what_filtered_cleaned_product.csv', 'what_filtered_version.csv',
    'what_filtered_op_sys.csv', 'what_filtered_component.csv',
    'what_filtered_severity.csv'
]

# File to concatenate as the first three columns
first3_file = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/Filter-Sorted/first3.csv'

# Initialize a list to store data from each file
data = []

# Read first3.csv and store its data
first3_data = []
first3_file_path = os.path.join(csv_path, first3_file)
with open(first3_file_path, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        first3_data.append(row)

# Read each what_* file and store its data
for what_file in what_files:
    what_file_path = os.path.join(csv_path, what_file)
    with open(what_file_path, 'r') as f:
        reader = csv.reader(f)
        column_data = [row[1] for row in reader]  # Extracting the second column assuming index starts from 0
        data.append(column_data)

# Check if all lists have the same length
lengths = [len(column_data) for column_data in data]
if not all(length == lengths[0] for length in lengths):
    raise ValueError("CSV files have different number of rows. Please ensure they are consistent.")

# Transpose the data (combine rows into columns)
combined_data = zip(first3_data, *data)

# Write combined data to Dataset.csv
output_file = os.path.join(csv_path, 'Dataset.csv')
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    
    # Write headers assuming first3.csv has no header
    writer.writerow(['Key1', 'Key2', 'Key3'] + ['Column{}'.format(i+1) for i in range(len(what_files))])

    # Write data
    for row in combined_data:
        writer.writerow(row)

print("Dataset.csv has been created successfully.")
