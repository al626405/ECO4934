import pandas as pd

# Load the dataset
df = pd.read_csv("/home/Alexis/Database/Dataset.csv")

# Select the columns to convert to dummy variables
columns_to_dummify = ['current_resolution', 'current_status', 'priority', 'product', 'version', 'op_sys', 'component', 'severity']

# Create dummy variables
df_dummies = pd.get_dummies(df, columns=columns_to_dummify)

# Save the resulting DataFrame to a new CSV file
df_dummies.to_csv("/home/Alexis/Database/Dataset_dummies.csv", index=False)

# Print the first few rows to check the result
print(df_dummies.head())
