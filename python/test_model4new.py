import tkinter as tk
from tkinter import ttk
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib
import numpy as np

# Load the trained Logistic Regression model
model = joblib.load('logistic_regression_model.pkl')

# Load the StandardScaler used during training
scaler = joblib.load('standard_scaler.pkl')

# Function to update the predicted health label
def update_health_prediction(*args):
    try:
        temperature = temp_slider.get()
        humidity = humidity_slider.get()

        # Update the value labels
        temp_value_label.config(text=f"Temperature: {int(temperature)}")
        humidity_value_label.config(text=f"Humidity: {int(humidity)}")

        # Preprocess features using the same StandardScaler used during training
        X_scaled = scaler.transform([[temperature, humidity]])

        # Predict health status
        prediction = model.predict(X_scaled)

        # Update the predicted health label
        if prediction[0] == 1:
            prediction_label.config(text="Predicted Health: Good")
        else:
            prediction_label.config(text="Predicted Health: Poor")
    except ValueError:
        pass

# Function to predict health status
def predict_health():
    temperature = temp_slider.get()
    humidity = humidity_slider.get()

    # Preprocess features using the same StandardScaler used during training
    X_scaled = scaler.transform([[temperature, humidity]])

    # Predict health status
    prediction = model.predict(X_scaled)

    # Update the predicted health label
    if prediction[0] == 1:
        prediction_label.config(text="Predicted Health: Good")
    else:
        prediction_label.config(text="Predicted Health: Poor")

# Create a Tkinter window
root = tk.Tk()
root.title("Health Prediction")

# Create and place temperature slider
temp_label = ttk.Label(root, text="Temperature (Celcius):")
temp_label.pack()
temp_slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=update_health_prediction)
temp_slider.set(25)  # Initial value
temp_slider.pack()

# Create and place humidity slider
humidity_label = ttk.Label(root, text="Humidity (%):")
humidity_label.pack()
humidity_slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=update_health_prediction)
humidity_slider.set(50)  # Initial value
humidity_slider.pack()

# Create value labels for temperature and humidity
temp_value_label = ttk.Label(root, text="Temperature: 25")
temp_value_label.pack()
humidity_value_label = ttk.Label(root, text="Humidity: 50")
humidity_value_label.pack()

# Create predict button
predict_button = ttk.Button(root, text="Predict", command=predict_health)
predict_button.pack()

# Create label for displaying predicted health
prediction_label = ttk.Label(root, text="Predicted Health:")
prediction_label.pack()

# Run the Tkinter main loop
root.mainloop()
