# Stroke Prediction

## Business Problem

According to the World Health Organization (WHO) stroke is the 2nd leading cause of death and long-term disability worldwide, responsible for approximately 11% of total deaths. Early detection and intervention are critical to improving patient outcomes and reducing healthcare costs. However, many hospitals face challenges in accurately predicting stroke risk due to a lack of integrated tools and resources, leading to delayed diagnosis and treatment.

## How Machine Learning Predictive Model Helps?

Your machine learning-based stroke prediction model addresses this problem by analyzing patient data to accurately assess the risk of stroke. By integrating this model into hospital systems, it can:

 - Early Detection: Provide real-time risk assessment for patients, enabling early identification of those at high risk of stroke.
 - Improved Patient Outcomes: Allow healthcare providers to implement preventive measures or early interventions, potentially reducing stroke incidents and improving recovery rates.
 - Resource Optimization: Help hospitals allocate resources more efficiently by focusing attention on high-risk patients, reducing unnecessary tests and hospital stays.
 - Personalized Care: Offer tailored recommendations based on individual risk profiles, enhancing patient care and engagement.

By implementing your model, hospitals can enhance clinical decision-making, improve patient outcomes, and optimize operational efficiency, ultimately contributing to better overall healthcare delivery.

Attribute Information
1) id: unique identifier
2) gender: "Male", "Female" or "Other"
3) age: age of the patient
4) hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
5) heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
6) ever_married: "No" or "Yes"
7) work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
8) Residence_type: "Rural" or "Urban"
9) avg_glucose_level: average glucose level in blood
10) bmi: body mass index
11) smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"*
12) stroke: 1 if the patient had a stroke or 0 if not

## FOLDER STRUCTURE
- codes: This folder contains the python files
    - train.py: This file reads the data and builds the best model (Logistic Regression). Please refer to the Modelling.ipynb in the notebook folder, how we select this LR.
    - predict.py: Flask app
    - test.py: Used to test the Flask app
    - lambda_function.py
    - test_lambda_local.py
    - test_lambda_main.py 

- data: This folder contains the data file used for the project.

- models: This folder contains the pickled models saved.

- notebooks: This folder contains the jupyter notebook(s) created. It contains the EDA and modelling steps taken to select the best model. 


## Set up Environment

After cloning the [repository](https://github.com/soumikghosal/Capstone-Project-1), follow the below steps:

Open cmd and navigate to the cloned local repository folder and create a virtual environment with the desired environment name.
```
virtualenv capstone_1
```
Activate the environment
```
capstone_1\Scripts\activate
```
Installl the required python packages
```
python install -r requirement.txt
```

# Running and Testing Service Locally with Flask

*** Note: Please rename Dockerfile as Dockerfile_1 and Dockerfile_2 as Dockerfile (in this order)

Build the docker container.
```
docker build -t capstone_test_1 .
```
Run the docker container
```
docker run -it --rm -p 9696:9696 capstone_test_1:latest
```
Testing the service
```
python scripts\test.py
```

## Running and Testing AWS Lambda Locally and Remotely

*** Note: If you ran the previous section then please rename Dockerfile as Dockerfile_2 and Dockerfile_1 as Dockerfile (in this order) or else run following steps.

Build the docker container.
```
docker build -t capstone_test_1 .
```
Run the docker container
```
docker run -it --rm -p 8080:8080 capstone_test_1:latest
```
Testing the service locally at: http://localhost:8080/2015-03-31/functions/function/invocations
```
python scripts\test_lambda_local.py
```

If you dont have an AWS account please go through this (video)[https://www.youtube.com/watch?v=kBch5oD5BkY&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=87]. It will cover:
- Create a repository and login to Docker
- Publishing the image to AWS ECR
- Creating AWS Lambda function
- Testing the function from the AWS Console

** Note: You will need to configure AWS CLI

Once this is done follow this (video)[https://www.youtube.com/watch?v=wyZ9aqQOXvs&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=88]. It covers how to expose the Lambda using API Gateway


Testing the service remotely: I have already hosted this service via AWS Lambda function at: https://exkg23rhe2.execute-api.us-east-2.amazonaws.com/capstone-1/predict
Feel free to test it by running the below command. The url is already set in the test_lambda_main.py file. If you wish to test your app, replace the url in this file and run the same below command.

```
python scripts\test_lambda_main.py
```

