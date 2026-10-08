import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# Load dataset
data = pd.read_csv("dataset/student_performance.csv")

# Features
X = data[
    [
        "Study_Hours",
        "Attendance",
        "Assignment_Score",
        "Previous_Marks"
    ]
]

# Target
y = data["Result"]

# Convert Pass/Fail into 1/0
y = y.map({"Fail": 0, "Pass": 1})

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Training Completed")
print("-------------------------")
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Fail", "Pass"]
))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# Save trained model
with open("trained_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nTrained model saved as trained_model.pkl")