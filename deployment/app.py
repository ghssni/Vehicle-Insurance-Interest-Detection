import streamlit as st
import EDA
import prediction

navigation = st.sidebar.selectbox('Choose Page:',('EDA', 'Predict Insurance Interest'))

if navigation == 'Predict Insurance Interest':
    prediction.run()
else:
    EDA.run()
    