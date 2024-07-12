import csv
import os

# Define the path to the CSV files
csv_path = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/Filter-Sorted/'

# Input and output file names
input_file = 'sorted_cleaned_reports.csv'
output_file = 'primarykeys.csv'

# Function to extract specific columns
def extract_columns(input_path, output_path, columns):
    with open(input_path, 'r') as infile, open(output_path, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            extracted_row = [row[i] for i in columns]
            writer.writerow(extracted_row)

# Main script
def main():
    input_path = os.path.join(csv_path, input_file)
    output_path = os.path.join(csv_path, output_file)
    
    # Indices of the columns to be extracted (0-based)
    columns_to_extract = [0, 3, 4]
    
    extract_columns(input_path, output_path, columns_to_extract)
    
    print(f"Columns extracted successfully. Output saved to '{output_file}'.")

if __name__ == "__main__":
    main()
