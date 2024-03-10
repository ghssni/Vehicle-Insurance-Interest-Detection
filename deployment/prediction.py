import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as ps
import numpy as np
import pickle

# Load file model
with open('svc_grid.pkl', 'rb') as file_1:
  svc_gridcv_best = pickle.load(file_1)

def run():
  st.title('Vehicle Insurance Interest Prediction')

  st.markdown('---')
  st.subheader('This Page Help You to Predict Customer Health Insurance Who Will Interested to Our Vehicle Insurance')
  st.write('Created by Sani')
  st.markdown('---')
  # Buat Form
  with st.form(key='Form Parameter'):
    age = st.number_input('Age', min_value=0, max_value=70,step=1)
    gender = st.selectbox('Gender', ('Male','Female'),index=0)
    rgc = st.number_input('Region Code', min_value=0.0, max_value=200.0,step=1.0)
    st.markdown('---')
    st.write('## Insurance Information')
    ap = st.number_input('Insurance Premi', min_value=0, max_value=1000000,step=100)
    psc = st.slider('Policy Sales Channel', 0.0,200.0,40.0)
    vt = st.number_input('Day Longevity', min_value=0, max_value=300,step=1)
    st.markdown('---')
    st.write('## Vehicle Information')
    pi = st.selectbox('Previously Insured',('Yes','No'),index=0)
    dl = st.selectbox('Having Driving License',('Yes','No'),index=0)
    va = st.selectbox('Vehicle Age',('< 1 Year', '1-2 Year', '> 2 Years'),index=0)
    vd = st.selectbox('Vehicle Damage in The Past',('Yes','No'),index=0)
    submitted= st.form_submit_button("predict")

  #Save Data
  data = {
      'id': 0,
      'gender': gender,
      'age': age,
      'driving_license': dl,
      'region_code': rgc,
      'previously_insured': pi,
      'vehicle_age': va,
      'vehicle_damage':vd ,
      'annual_premium': ap,
      'policy_sales_channel': psc,
      'vintage': vt,
  }

  # Save to DataFrame
  data_inf = pd.DataFrame([data])
  st.dataframe(data_inf)

  # Region Code Category
  list_small = [25.0, 44.0]
  list_med = [24.0, 7.0, 18.0, 3.0, 35.0, 39.0, 52.0, 29.0, 41.0, 40.0, 5.0, 20.0, 11.0, 45.0, 1.0, 46.0, 48.0, 31.0, 33.0, 12.0, 8.0, 43.0, 14.0, 13.0, 47.0, 0.0, 32.0, 9.0, 36.0, 37.0, 34.0, 49.0, 42.0, 27.0, 30.0, 26.0, 15.0, 2.0, 21.0, 17.0, 6.0, 16.0, 22.0, 50.0, 10.0]  
  list_high = [38.0, 28.0, 19.0, 4.0, 23.0, 51.0]

  # Function to category region code
  def final(x):
    if x in list_small:
      return "small chance"
    elif x in list_med:
      return "medium chance"
    elif x in list_high:
      return "high chance"

  # Input to dataframe
  data_inf['reg_code_cat'] = data_inf['region_code'].apply(final)

  # For Policy Sales Channel Category
  # List
  list_small = [57.0, 25.0, 26.0, 44.0, 42.0, 59.0, 94.0, 10.0, 124.0, 17.0, 147.0, 56.0, 91.0, 122.0, 12.0, 62.0, 69.0, 54.0, 55.0, 45.0, 13.0, 89.0, 49.0, 23.0, 40.0, 35.0, 111.0, 145.0, 24.0, 78.0, 114.0, 47.0, 29.0, 103.0, 86.0, 92.0, 125.0, 109.0, 116.0, 131.0, 7.0, 58.0, 20.0, 30.0, 52.0, 93.0, 148.0, 60.0, 14.0, 9.0, 39.0, 37.0, 138.0, 61.0, 32.0, 128.0, 130.0, 139.0, 110.0, 11.0, 135.0, 15.0, 16.0, 19.0, 120.0, 51.0, 8.0, 21.0, 97.0, 73.0, 127.0, 129.0, 65.0, 113.0, 140.0, 132.0, 153.0, 88.0, 64.0, 66.0, 22.0, 63.0, 48.0, 119.0, 98.0, 133.0, 107.0, 18.0, 1.0, 151.0, 152.0, 108.0, 160.0, 159.0, 102.0, 34.0, 46.0, 146.0, 41.0, 38.0, 149.0, 82.0, 143.0, 33.0, 83.0, 96.0, 105.0, 144.0, 79.0, 71.0, 74.0, 6.0, 70.0, 67.0, 126.0, 95.0, 118.0, 117.0, 104.0, 76.0, 115.0, 75.0, 134.0, 112.0, 99.0, 137.0, 50.0, 84.0]  
  list_med = [27.0, 28.0, 36.0, 155.0, 163.0, 3.0, 121.0, 101.0, 87.0, 80.0, 81.0, 158.0, 90.0, 157.0, 31.0, 100.0, 68.0, 2.0, 154.0, 150.0, 106.0, 53.0, 136.0, 156.0, 4.0]  
  list_high = [123.0, 43.0]

  # Function to categorize
  def final(x):
    if x in list_small:
      return "small chance"
    elif x in list_med:
      return "medium chance"
    elif x in list_high:
      return "high chance"
  # Input to dataframe
  data_inf['policy_sales_channel_cat'] = data_inf['policy_sales_channel'].apply(final)

  # Function for categorize age
  def umur(x):
    if x <= 25:
      return "young adult"
    elif x <= 44:
      return "adult"
    elif x <= 59:
      return "middle old"
    else:
      return "old"

  # Apply to new column
  data_inf['age_cat'] = data_inf['age'].apply(umur)

  # Replace Value From form
  data_inf['driving_license'] = data_inf['driving_license'].replace(['Yes', 'No'], [1,0])
  data_inf['previously_insured'] = data_inf['previously_insured'].replace(['Yes', 'No'], [1,0])

  if submitted:
      y_pred_final = svc_gridcv_best.predict(data_inf)
      if y_pred_final == 0:
        st.write('# Interested to Vehicle Insured')
      else:
        st.write('# Not Interested to Vehicle Insured')

if __name__ == '__main__':
  run()