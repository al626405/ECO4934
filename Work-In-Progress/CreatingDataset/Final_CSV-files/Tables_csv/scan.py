import os
import csv

# Directory where CSV files are located
csv_directory = '/var/lib/mysql/Final_Project/Final_CSV-files/Tables_csv/'

# Function to check if a string is numeric
def is_numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Function to check if first two columns in a CSV file contain numeric values
def check_csv_for_numeric_columns(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2 and is_numeric(row[0]) and is_numeric(row[1]):
                return True
    return False

# Main function to search through CSV files
def search_csv_files(directory):
    files_with_numeric_columns = []
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            if check_csv_for_numeric_columns(file_path):
                files_with_numeric_columns.append(filename)
    return files_with_numeric_columns

# Search for files with numeric values in the first two columns
files_found = search_csv_files(csv_directory)

# Print the results
if files_found:
    print("Files with numeric values in the first two columns:")
    for file in files_found:
        print(file)
else:
    print("No files found with numeric values in the first two columns.")
