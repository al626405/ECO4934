import csv
import os

# Define the path to the CSV file
csv_file_path = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/Filter-Sorted/sorted_cleaned_reports.csv'

# Paths for output CSV files
output_col2_path = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/Filter-Sorted/Filtered/reportcol2.csv'
output_col3_path = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/Filter-Sorted/Filtered/reportcol3.csv'

# Initialize lists to store data for columns 2 and 3
column2_data = []
column3_data = []

# Read from sorted_cleaned_reports.csv
with open(csv_file_path, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        # Append the second column (index 1) to column2_data
        column2_data.append([row[1]])
        # Append the third column (index 2) to column3_data
        column3_data.append([row[2]])

# Write to reportcol2.csv
with open(output_col2_path, 'w', newline='') as f2:
    writer2 = csv.writer(f2)
    writer2.writerows(column2_data)

# Write to reportcol3.csv
with open(output_col3_path, 'w', newline='') as f3:
    writer3 = csv.writer(f3)
    writer3.writerows(column3_data)

print("Extraction completed successfully.")
