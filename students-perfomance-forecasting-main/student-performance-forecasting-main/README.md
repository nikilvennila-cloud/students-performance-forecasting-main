# Student Performance Prediction

## Project Overview

Student Performance Prediction is a Machine Learning based web application that predicts whether a student is likely to **Pass** or **Fail** based on their academic details.

The system uses study hours, attendance, assignment score, and previous marks as input features and provides a prediction using a trained Machine Learning model.

## Features

* Student performance prediction
* Study hours input
* Attendance percentage input
* Assignment score input
* Previous marks input
* Pass/Fail prediction
* Input validation
* FastAPI backend
* Simple and responsive web interface

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* FastAPI
* Uvicorn

### Machine Learning

* Pandas
* Scikit-learn
* Pickle

## Project Structure

```text
predictive_modeling_ml/
│
├── dataset/
│   └── student_performance.csv
│
├── model/
│   └── train_model.py
│
├── visualization/
│
├── api.py
├── index.html
├── trained_model.pkl
├── requirements.txt
└── README.md
```

## Input Features

The model uses the following features:

| Feature          | Description                    |
| ---------------- | ------------------------------ |
| Study Hours      | Number of hours spent studying |
| Attendance       | Student attendance percentage  |
| Assignment Score | Assignment score               |
| Previous Marks   | Previous academic marks        |

## How to Run

### 1. Install Dependencies

Open PowerShell in the project folder:

```powershell
pip install -r requirements.txt
```

### 2. Start the Backend

Run:

```powershell
& "C:\Users\prith\AppData\Local\Python\pythoncore-3.14-64\python.exe" -m uvicorn api:app --reload
```

Backend will run at:

```text
http://127.0.0.1:8000
```

### 3. Open the Frontend

Open `index.html` in a web browser.

Enter the student's details and click:

**Predict Performance**

## API Endpoint

### Health Check

```text
GET /
```

### Prediction

```text
POST /predict
```

Example request:

```json
{
    "study_hours": 6,
    "attendance": 85,
    "assignment_score": 80,
    "previous_marks": 70
}
```

Example response:

```json
{
    "prediction": "Pass"
}
```

## Prediction Output

The application provides one of two results:

* **Pass**
* **Fail**

## Project Status

The Student Performance Prediction application is successfully connected between the frontend, FastAPI backend, and trained Machine Learning model.
