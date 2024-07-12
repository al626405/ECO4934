import csv
import os

# Define the path to the CSV files
csv_path = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/'

# List of CSV files to be filtered
csv_files = [
    'priority.csv', 'cleaned_product.csv',
    'version.csv', 'op_sys.csv', 'component.csv', 'severity.csv'
]

# File names
cleaned_reports_file = 'cleaned_reports.csv'
filtered_ids_file = 'filtered_ids.csv'

# Step 1: Extract the first column of cleaned_reports.csv and save it to a new CSV file
def extract_first_column(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            writer.writerow([row[0]])

# Step 2: Filter other CSV files based on the extracted IDs and sort the rows
def filter_and_sort_csv_files(ids_file, csv_files, csv_path):
    with open(ids_file, 'r') as idfile:
        ids = set(row[0] for row in csv.reader(idfile))
    
    for file in csv_files:
        input_path = os.path.join(csv_path, file)
        output_path = os.path.join(csv_path, f"filtered_{file}")
        
        with open(input_path, 'r') as infile:
            reader = csv.reader(infile)
            filtered_rows = [row for row in reader if row[0] in ids]
        
        # Sort the filtered rows based on the first column (assumed to be numeric)
        filtered_rows.sort(key=lambda x: int(x[0]))
        
        with open(output_path, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(filtered_rows)

# Step 3: Main script
def main():
    # Extract the first column of cleaned_reports.csv
    cleaned_reports_path = os.path.join(csv_path, cleaned_reports_file)
    filtered_ids_path = os.path.join(csv_path, filtered_ids_file)
    extract_first_column(cleaned_reports_path, filtered_ids_path)

    # Filter and sort other CSV files based on the extracted IDs
    filter_and_sort_csv_files(filtered_ids_path, csv_files, csv_path)

    print("Filtering and sorting complete. Filtered files are saved with 'filtered_' prefix.")

if __name__ == "__main__":
    main()
