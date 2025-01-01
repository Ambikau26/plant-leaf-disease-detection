import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Load the model
model = tf.keras.models.load_model('keras_Model.h5')

# Load the label names
with open('labels.txt', 'r') as f:
    label_names = f.read().splitlines()

# Load and preprocess the image
img_path = '2.jpg'  # Replace with the path to your image

# Load image and resize to the target size (150x150)
img = image.load_img(img_path, target_size=(150, 150))

# Convert the image to an array and expand dimensions
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

# Normalize the image (divide by 255 to scale pixel values to [0, 1])
x = x / 255.0

# Predict the class of the image
predictions = model.predict(x)

# Get the class index with the highest probability
class_index = np.argmax(predictions[0])

# Get the predicted class name
class_name_predicted = label_names[class_index]

# Print the predicted class
print('Predicted class:', class_name_predicted)
