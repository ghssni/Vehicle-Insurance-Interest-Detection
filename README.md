# Vehicle Insurance Interest Detection

This repository delves into predicting customer interest in vehicle insurance amongst existing health insurance holders. It explores historical data (past year) to build a model that identifies potential customers for vehicle insurance cross-selling opportunities.

## Project Overview
- Predict Vehicle Insurance Interest: Build a model to predict which health insurance policyholders are most likely to be interested in purchasing vehicle insurance from the same company.
- Uncover Key Factors: Identify factors influencing customer decisions to purchase vehicle insurance alongside health insurance.
- Optimize Marketing Strategies: Leverage insights from the model to tailor marketing campaigns for efficient cross-selling of vehicle insurance.

## Tools and Technologies
- Python
- Jupyter Notebook
- Pandas
- Matplotlib
- Seaborn
- Tableau
- Scikit-Learn

## File Description
- `Vehicle_Insurance_Interest_Detection.ipynb` : Jupyter Notebook containing the code used for data cleaning, exploratory data analysis, feature engineering, model training & evaluation and model improvement.
- `Vehicle_Insurance_Interest_Detection_Inference.ipynb` : Jupyter Notebook containing the code for model inference testing.
- `Vehicle_Insurance_Interest_Detection_Data.csv`: CSV file containing the historical data of Customers Health Insurance with features relevant to predicting vehicle insurance interest.
- `svc_gridcv_best.pkl` : Best Model with Best Parameter

## Algorithm Used
- K-Nearest Neighbors 
- Support Vector Machines Classifier
- Decision Tree 
- Random Forest 
- XG Boost

## Exploratory Data Analysis Recap
- The data in the target column is not balanced with a percentage split of 88% and 12%.
- Customers who are interested in insurance are dominated by male gender.
- Customers who are interested in insurance have a lower average annual premium with a value of 30419.
- Customers who are interested in our insurance are on average 43 years old with an age range of adult (26-44 years).
- Customers who are interested in our insurance also have the most vehicles with a vehicle age of 1-2 years. 

## Conclussion
We compared five models to predict customer interest in vehicle insurance. The SVC model emerged as the best option due to its strong evaluation results. It achieved a high AUC value and the best cross-validation score among all models.

The SVC model demonstrates good accuracy with a precision train value of 80% and a resampled test precision of 74%. This means that if the model predicts 100 customers as interested in vehicle insurance, approximately 74 of them are likely to be genuinely interested.

## Suggestion
The response column in the Health Insurance Cross-Sell Prediction dataset can be used to get various business insights that can help companies to improve their cross-selling strategy.
- Customers who are interested in vehicle insurance We can do targeting so that our insurance sales are not misdirected.
- Customers who are not interested in vehicle insurance We can influence them without making them feel disturbed by the marketing that is being done so that it will increase the chance of customers' interest in vehicle insurance.

## Acknowledgements
The Health Insurance Cross Sell Prediction data used in this project was obtained from [Kaggle](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction?select=test.csv)

Dashboard visualization for this project on [Tableau]()

Model Deployment for this project on [Hugging Face](https://huggingface.co/spaces/ghtyas/InsurancePredict)
