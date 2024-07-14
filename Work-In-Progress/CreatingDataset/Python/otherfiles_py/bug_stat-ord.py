import csv
import os
from datetime import datetime

# Define the path to the CSV files
csv_path = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/'

# File names
cleaned_reports_file = 'bug_status.csv'
sorted_cleaned_reports_file = 'sorted_bug_status.csv'

# Function to sort the rows based on the datetime in the fourth column
def sort_csv_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Skip the header if present
        sorted_rows = sorted(reader, key=lambda x: datetime.strptime(x[3], '%Y-%m-%d %H:%M:%S'))
    
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)  # Write the header back
        writer.writerows(sorted_rows)

# Main script
def main():
    # Sort bug_status.csv
    cleaned_reports_path = os.path.join(csv_path, cleaned_reports_file)
    sorted_cleaned_reports_path = os.path.join(csv_path, sorted_cleaned_reports_file)
    sort_csv_file(cleaned_reports_path, sorted_cleaned_reports_path)

    print("Sorting complete. Sorted file is saved as 'sorted_bug_status.csv'.")

if __name__ == "__main__":
    main()
