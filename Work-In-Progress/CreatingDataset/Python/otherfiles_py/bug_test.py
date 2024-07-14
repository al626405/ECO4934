import csv
import os
from datetime import datetime

# Define the path to the CSV files
csv_path = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/'

# File names
cleaned_reports_file = 'bug_status.csv'
sorted_cleaned_reports_file = 'sorted_bug_status.csv'

# Function to convert datetime string to datetime object for sorting
def convert_to_datetime(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

# Function to sort the rows based on the third column (assuming date/time)
def sort_csv_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        reader = csv.reader(infile)
        sorted_rows = sorted(reader, key=lambda x: convert_to_datetime(x[3]))
    
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(sorted_rows)

# Main script
def main():
    # Sort bug_status.csv
    cleaned_reports_path = os.path.join(csv_path, cleaned_reports_file)
    sorted_cleaned_reports_path = os.path.join(csv_path, sorted_cleaned_reports_file)
    sort_csv_file(cleaned_reports_path, sorted_cleaned_reports_path)

    print(f"Sorting complete. Sorted file is saved as '{sorted_cleaned_reports_file}'.")

if __name__ == "__main__":
    main()
