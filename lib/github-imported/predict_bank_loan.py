import dataiku
import pandas as pd
from dataiku import pandasutils as pdu
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset
dataset = dataiku.Dataset("your_dataset_name")
df = dataset.get_dataframe()

# Assuming 'target' is the column you want to predict
X = df.drop(columns=['target'])
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")

import joblib
model_folder = dataiku.Folder("your_model_folder_id")
joblib.dump(rf_model, model_folder.get_path() + "/random_forest_model.pkl")
