import h5py
import numpy as np
import tensorflow as tf

# Load the HDF5 model
h5_model_path = 'logistic_regression_model.h5'
model = tf.keras.models.load_model(h5_model_path)

# Extract weights and biases from the model layers
weights = []
biases = []

for layer in model.layers:
    if isinstance(layer, tf.keras.layers.Dense):
        weights.append(layer.get_weights()[0])
        biases.append(layer.get_weights()[1])

# Generate C/C++ code for weights and biases
c_code = '''
#ifndef MODEL_H
#define MODEL_H

// Weights and biases
'''

for i, (w, b) in enumerate(zip(weights, biases)):
    c_code += f'static const float layer_{i}_weights[] = {{'
    c_code += ', '.join(map(str, w.flatten()))
    c_code += '};\n'

    c_code += f'static const float layer_{i}_biases[] = {{'
    c_code += ', '.join(map(str, b))
    c_code += '};\n'

c_code += '''
#endif
'''

# Save the C/C++ code to a file
c_file_path = 'model_c.h'
with open(c_file_path, 'w') as f:
    f.write(c_code)
