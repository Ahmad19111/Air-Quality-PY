import streamlit as st
import pandas as pd
import joblib
import requests

API_KEY = st.secrets["API_KEY"]
# 1. Load the pre-trained Random Forest model
# This model was trained on real-world data from India
model = joblib.load("models/air_quality_model_v1.pkl")

# 2. Set up the Web App UI
st.title("AI Air Quality Predictor")
#st.write("Enter the sensor readings below to predict the Air Quality category.")

# 3. User input fields for the 5 key pollutants
# Adjusted min/max/default values to reflect realistic sensor ranges
# PM2_5 = st.number_input("Enter PM2.5", min_value=0.0, max_value=500.0, value=30.0)
# NO2 = st.number_input("Enter NO2", min_value=0.0, max_value=200.0, value=40.0)
# CO = st.number_input("Enter CO", min_value=0.0, max_value=50.0, value=1.0)
# SO2 = st.number_input("Enter SO2", min_value=0.0, max_value=200.0, value=10.0)
# O3 = st.number_input("Enter O3", min_value=0.0, max_value=200.0, value=20.0)

#city = st.text_input("Enter a German City", max_chars= 30)
city = st.text_input("Enter any City in the World", max_chars= 30)
if city == "":
    st.warning("Plase Enter a City name")
    st.stop()
#country = "DE"

# 4. Prediction Logic
if st.button("Air Quality Forecast 🚀"):
    #url_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit=1&appid={API_KEY}"
    url_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    response_city = requests.get(url_city)
    data_city = response_city.json()

    if len(data_city) == 0:
        st.error("City not found! Please check the spelling.")
        st.stop()

    lat = data_city[0]["lat"]
    lon = data_city[0]["lon"]

    url_pollution = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    response_pollution = requests.get(url_pollution)
    data_pollution = response_pollution.json()

#{'coord': {'lon': 9.2053, 'lat': 52.329}, 'list': [{'main': {'aqi': 2}, 'components': {'co': 215.07, 'no': 0, 'no2': 10.86, 'o3': 49.45, 'so2': 0.65, 'pm2_5': 22.75, 'pm10': 28.23, 'nh3': 2.92}, 'dt': 1773970819}]}

    PM2_5 = data_pollution["list"][0]["components"]["pm2_5"]
    NO2 = data_pollution["list"][0]["components"]["no2"]
    CO = data_pollution["list"][0]["components"]["co"]/1000
    SO2 = data_pollution["list"][0]["components"]["so2"]
    O3 = data_pollution["list"][0]["components"]["o3"]




    # Format the input exactly as the model expects (same column names)
    input_data = pd.DataFrame({
        "PM2.5": [PM2_5],
        "NO2": [NO2],
        "CO": [CO],
        "SO2": [SO2],
        "O3": [O3]
    })
    st.write("🕵️‍♂️ Raw Data received from API:", input_data)
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