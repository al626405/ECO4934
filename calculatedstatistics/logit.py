import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Load your dataset containing 'success_rate' and other relevant features
dataset = pd.read_csv("/path/to/your/dataset.csv")

# Select relevant features and target variable
X = dataset[['success_rate', 'other_feature1', 'other_feature2', ...]]
y = dataset['target_variable']  # Replace 'target_variable' with your actual target column

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize logistic regression model
model = LogisticRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Predict on the test data
y_pred = model.predict(X_test)

# Evaluate model performance
print(classification_report(y_test, y_pred))

# Analyze coefficients to understand the impact of 'success_rate'
coefficients = pd.DataFrame({'feature': X.columns, 'coefficient': model.coef_[0]})
print("Coefficient Summary:\n", coefficients)

# Interpret the impact of 'success_rate' based on its coefficient
# Positive coefficient suggests a positive impact, negative suggests a negative impact
