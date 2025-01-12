import cloudpickle
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify 
    
def predict_level(patient, pipe, lr_model):
    patient = pd.DataFrame(data=patient, index=[0])
    X_test = pipe.transform(patient)
    pred = lr_model.predict(X_test)
    # stroke: 1 if the patient had a stroke or 0 if not
    pred_label = ["not stroke" if ele==0 else "stroke" for ele in pred]
    return pred_label

with open('../models/stroke_pred_model.bin', 'rb') as f_in:
    pipe, lr_model = cloudpickle.load(f_in)
    
app = Flask('stroke-prediction')

@app.route('/')
def hello_world():
    return "<p>HWorld!</p>"

@app.route('/predict', methods=['POST'])
def predict():
    patient = request.get_json()
    prediction = predict_level(patient, pipe, lr_model)
    result = {'stroke_prediction': str(prediction)}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
 
 