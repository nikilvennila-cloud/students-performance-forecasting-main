import pickle
import pandas as pd

with open("trained_model.pkl", "rb") as file:
    model = pickle.load(file)

print("Predictive Model Loaded Successfully")
print("-----------------------------------")

study_hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance percentage: "))
assignment_score = float(input("Enter assignment score: "))
previous_marks = float(input("Enter previous marks: "))

input_data = pd.DataFrame({
    "Study_Hours": [study_hours],
    "Attendance": [attendance],
    "Assignment_Score": [assignment_score],
    "Previous_Marks": [previous_marks]
})

prediction = model.predict(input_data)

if prediction[0] == 1:
    print("\nPrediction: Pass")
else:
    print("\nPrediction: Fail")