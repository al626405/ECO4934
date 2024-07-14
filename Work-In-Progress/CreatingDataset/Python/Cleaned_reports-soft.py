import csv
import os

# Define the path to the CSV files
csv_path = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/'

# File names
cleaned_reports_file = 'cleaned_reports.csv'
sorted_cleaned_reports_file = 'sorted_cleaned_reports.csv'

# Function to sort the rows based on the first column
def sort_csv_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        reader = csv.reader(infile)
        sorted_rows = sorted(reader, key=lambda x: int(x[0]))
    
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(sorted_rows)

# Main script
def main():
    # Sort cleaned_reports.csv
    cleaned_reports_path = os.path.join(csv_path, cleaned_reports_file)
    sorted_cleaned_reports_path = os.path.join(csv_path, sorted_cleaned_reports_file)
    sort_csv_file(cleaned_reports_path, sorted_cleaned_reports_path)

    print("Sorting complete. Sorted file is saved as 'sorted_cleaned_reports.csv'.")

if __name__ == "__main__":
    main()
