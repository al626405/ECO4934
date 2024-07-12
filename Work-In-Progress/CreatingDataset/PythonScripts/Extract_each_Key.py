import csv
import os

# Define the path to the CSV files
csv_path = '/home/Alexis/Database/MySQL_Table_Creation/Final_Project/Final_CSV-files/Tables_csv1/Filter-Sorted/'

# File containing primary keys with multiple columns
primarykeys_file = 'primarykeys.csv'

# Initialize lists to store data for each column
id_data = []
when_data = []
who_data = []

# Read primarykeys.csv and extract data for each column
primarykeys_file_path = os.path.join(csv_path, primarykeys_file)
with open(primarykeys_file_path, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        id_data.append(row[0])     # Assuming id is the first column
        when_data.append(row[1])   # Assuming when is the second column
        who_data.append(row[2])    # Assuming who is the third column

# Write id_data to id.csv
id_file = os.path.join(csv_path, 'id.csv')
with open(id_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id'])  # Write header if needed
    writer.writerows([[id] for id in id_data])  # Write each id as a separate row

# Write when_data to when.csv
when_file = os.path.join(csv_path, 'when.csv')
with open(when_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['when'])  # Write header if needed
    writer.writerows([[when] for when in when_data])  # Write each when as a separate row

# Write who_data to who.csv
who_file = os.path.join(csv_path, 'who.csv')
with open(who_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['who'])  # Write header if needed
    writer.writerows([[who] for who in who_data])  # Write each who as a separate row

print("Columns extracted and saved to id.csv, when.csv, and who.csv successfully.")
