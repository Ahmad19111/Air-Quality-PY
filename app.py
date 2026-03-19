import streamlit as st
import pandas as pd
import joblib

# 1. Load the pre-trained Random Forest model
# This model was trained on real-world data from India
model = joblib.load("models/air_quality_model_v1.pkl")

# 2. Set up the Web App UI
st.title("AI Air Quality Predictor")
st.write("Enter the sensor readings below to predict the Air Quality category.")

# 3. User input fields for the 5 key pollutants
# Adjusted min/max/default values to reflect realistic sensor ranges
PM2_5 = st.number_input("Enter PM2.5", min_value=0.0, max_value=500.0, value=30.0)
NO2 = st.number_input("Enter NO2", min_value=0.0, max_value=200.0, value=40.0)
CO = st.number_input("Enter CO", min_value=0.0, max_value=50.0, value=1.0)
SO2 = st.number_input("Enter SO2", min_value=0.0, max_value=200.0, value=10.0)
O3 = st.number_input("Enter O3", min_value=0.0, max_value=200.0, value=20.0)

# 4. Prediction Logic
if st.button("Air Quality Forecast 🚀"):
    
    # Format the input exactly as the model expects (same column names)
    input_data = pd.DataFrame({
        "PM2.5": [PM2_5],
        "NO2": [NO2],
        "CO": [CO],
        "SO2": [SO2],
        "O3": [O3]
    })
    
    # Make the prediction
    prediction = model.predict(input_data)
    result = prediction[0]
    
    # 5. Display the result with appropriate colors and UX messages
    if result == "Good":
        st.success(f"Result: {result} - Fresh, excellent air! Breathe deeply 🌿")
    elif result == "Satisfactory":
        st.info(f"Result: {result} - Air is fresh, you can breathe 👍")
    elif result == "Moderate":
        st.warning(f"Result: {result} - Air quality is acceptable 😐")
    else:
        # Catches "Poor", "Very Poor", and "Severe" from the Indian Dataset
        st.error(f"Result: {result} - Warning: Bad Air quality, be careful! 😷")