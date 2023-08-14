import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib
import tensorflow as tf
from tensorflow import keras
import numpy as np

# Step 1: Load the data
data = pd.read_csv('newdata.csv')

# Step 2: Preprocess the data
features = data[['Temperature (Celcius)', 'Humidity (%)']]
target_column = 'Status'
target = data[target_column]

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Step 4: Preprocess features using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save the trained StandardScaler to a file
joblib.dump(scaler, 'standard_scaler.pkl')

# Step 5: Train a Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# Save the trained Logistic Regression model
joblib.dump(model, 'logistic_regression_model.pkl')

# Step 6: Convert the model to TensorFlow format
def build_keras_model():
    keras_model = keras.Sequential([
        keras.layers.Input(shape=X_train_scaled.shape[1]),
        keras.layers.Dense(1, activation='sigmoid')  # Sigmoid activation for binary classification
    ])
    return keras_model

keras_model = build_keras_model()
keras_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Reshape the Logistic Regression weights to match Keras dense layer shape
weights = [np.reshape(model.coef_[0], (-1, 1)), model.intercept_]
keras_model.layers[0].set_weights(weights)

# Save the Keras model in HDF5 format
keras_model.save('logistic_regression_model.h5')

# Step 7: Convert the TensorFlow model to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(keras_model)
tflite_model = converter.convert()

# Save the TensorFlow Lite model
with open('logistic_regression_model.tflite', 'wb') as f:
    f.write(tflite_model)

print("Conversion to TensorFlow Lite completed.")
