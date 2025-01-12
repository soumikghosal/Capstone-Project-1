import cloudpickle
import pandas as pd
import numpy as np
    
with open('stroke_pred_model.bin', 'rb') as f_in:
    pipe, lr_model = cloudpickle.load(f_in)

def predict_level(patient, pipe=pipe, lr_model=lr_model):
    patient = pd.DataFrame(data=patient, index=[0])
    X_test = pipe.transform(patient)
    pred = lr_model.predict(X_test)
    # stroke: 1 if the patient had a stroke or 0 if not
    pred_label = ["not stroke" if ele==0 else "stroke" for ele in pred]
    return pred_label

def lambda_handler(event, context):
       
    patient = {
        'gender': event['gender'],
        'age': event['age'],
        'hypertension': event['hypertension'],
        'heart_disease': event['heart_disease'],
        'ever_married': event['ever_married'],
        'work_type': event['work_type'],
        'residence_type': event['residence_type'],
        'avg_glucose_level': event['avg_glucose_level'],
        'bmi': event['bmi'],
        'smoking_status': event['smoking_status']
    } 
    
    result = predict_level(patient)
    return result














 
 