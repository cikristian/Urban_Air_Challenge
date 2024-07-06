pip install joblib
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle

st.title('Air Quality Predictor')
#st.image("""C:\Users\USER1\Desktop\download.jpeg""")
st.header('This app uses 4 inputs to predict air quality in cities around the world using a model built on satellite (Zindi) data. use the form below to get started!')
st.text("Created by Planet Protectors Study Group")

# Add navigation links in the sidebar
st.sidebar.selectbox("Navigation", ["Home", "About", "Contact"])

model = pickle.load(open('random_forest_model_four_features.pkl', 'rb'))

cols=['precipitable_water_entire_atmosphere', 'relative_humidity_2m_above_ground', 
      'specific_humidity_2m_above_ground', 'temperature_2m_above_ground']    

# Define the prediction function
def predict(precipitable_water_entire_atmosphere, relative_humidity_2m_above_ground, 
            specific_humidity_2m_above_ground, temperature_2m_above_ground):
    
    prediction = model.predict([[precipitable_water_entire_atmosphere, relative_humidity_2m_above_ground, 
            specific_humidity_2m_above_ground, temperature_2m_above_ground]])
    
    return prediction


precipitable_water_entire_atmosphere = st.number_input('Precipitable water', 0.00, 100.00)
relative_humidity_2m_above_ground = st.number_input('Relative humidity', 0.00, 100.00)
specific_humidity_2m_above_ground = st.number_input('Specific humidity', 0.00, 100.00)
temperature_2m_above_ground = st.number_input('Temperature', 0.00, 100.00)
gender = st.selectbox("gender", options=["male","female"])
age = st.slider("age", 0, 70)

if st.button('Predict Air Quality'):
    a_q = predict(precipitable_water_entire_atmosphere, relative_humidity_2m_above_ground, 
            specific_humidity_2m_above_ground, temperature_2m_above_ground)
    st.success(f'The predicted air quality is {a_q[0]:.2f} PM2.5')











    
    
    
    
    
    
    
    
    
    
    
