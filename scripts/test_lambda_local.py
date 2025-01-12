import requests

url = "http://localhost:8080/2015-03-31/functions/function/invocations"

client = {
    "gender": "Male",
    "age": 27.0,
    "hypertension": 0,
    "heart_disease": 0,
    "ever_married": "Yes",
    "work_type": "Private",
    "residence_type": "Urban",
    "avg_glucose_level": 28.69,
    "bmi": 36.6,
    "smoking_status": "formerly smoked",
    }

response = requests.post(url, json=client).json()

print(response)