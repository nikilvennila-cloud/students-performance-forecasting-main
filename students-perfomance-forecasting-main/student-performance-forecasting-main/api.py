from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI(title="Student Performance Prediction API")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained model
with open("trained_model.pkl", "rb") as file:
    model = pickle.load(file)


class StudentData(BaseModel):
    study_hours: float
    attendance: float
    assignment_score: float
    previous_marks: float


@app.get("/")
def home():
    return {
        "message": "Student Performance Prediction API is running"
    }


@app.post("/predict")
def predict(data: StudentData):

    input_data = pd.DataFrame({
        "Study_Hours": [data.study_hours],
        "Attendance": [data.attendance],
        "Assignment_Score": [data.assignment_score],
        "Previous_Marks": [data.previous_marks]
    })

    prediction = model.predict(input_data)

    result = "Pass" if prediction[0] == 1 else "Fail"

    return {
        "prediction": result
    }