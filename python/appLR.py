import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib
import numpy as np

# Load the trained Logistic Regression model
model = joblib.load('logistic_regression_model.pkl')

# Load the StandardScaler used during training
scaler = joblib.load('standard_scaler.pkl')

# Function to predict health status
def predict_health(temperature, humidity):
    # Preprocess features using the same StandardScaler used during training
    X_scaled = scaler.transform([[temperature, humidity]])

    # Predict health status
    prediction = model.predict(X_scaled)

    return prediction[0]

# Streamlit App
def main():
    st.title("Health Prediction")

    # Temperature slider
    temperature = st.slider("Temperature (Celcius)", 0, 100, 25)

    # Humidity slider
    humidity = st.slider("Humidity (%)", 0, 100, 50)

    # Display selected values
    st.write(f"Selected Temperature: {temperature}")
    st.write(f"Selected Humidity: {humidity}")

    # Predict button
    if st.button("Predict"):
        prediction = predict_health(temperature, humidity)
        if prediction == 1:
            st.write("Predicted Health: Good")
        else:
            st.write("Predicted Health: Poor")

if __name__ == "__main__":
    main()