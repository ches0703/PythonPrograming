# Handwritten Digits Recognition
# Make_CNN_Model.py
"""
Project : Handwritten Digits Recognition
Author: Eun-seong Choi
Date of last update: 2022 / 12 / 07
Update list:
    - v1.1 : 12 / 01
        Download & Add in Dir : mnist.npz
        Applcation Pythne file : Handwritten_Digits_Recognition_GUI.py
        Add commit
"""
# Basical import : For use deeplearning
import tensorflow as tf
import keras
# Import keras's data Set
from keras.datasets import mnist
# For use keras model : Sequential
from keras.models import Sequential
# Keras Sequential Model
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
# Keras utils
kr_utils = tf.keras.utils   # == from keras.utils import to_categorical

from keras import backend as k
import numpy as np                  # Mathematical processing module
import pandas as pd                 # Data processing module
import matplotlib.pyplot as plt     # Data visualization

# Load dataset directly from keras library
print("Loading MNIST data . . . .")
mnist_npz_path = "mnist.npz"
(X_train, y_train), (X_test, y_test) = mnist.load_data(path=mnist_npz_path)

# Setting digit name
digit_names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Print Mnist Sample Data
plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_train[i], cmap="gray")
    plt.title(digit_names[y_train[i]])
    plt.axis('off')
plt.show()

# Reshape format [samples][width][height][channels]
print("Reshaping format . . . .")
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32')
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype('float32')

# Converts a class vector (integer) to binary class matrix
print("Converting class vector . . . .")
# Converts a class vector (integers) to binary class matrix.
y_train = tf.keras.utils.to_categorical(y_train)
y_test = tf.keras.utils.to_categorical(y_test)

# Normalize inputs
X_train = X_train / 255
X_test = X_test / 255

# Define a CNN model
print("Preparing a CNN model . . . .")
num_classes = 10
model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation="relu", input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, (3, 3), activation="relu"),
    Flatten(),
    Dense(256, activation="relu"),
    Dropout(0.5),
    Dense(num_classes, activation="softmax")])
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Fit the model
print("Fitting the model . . . .")
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20,
          batch_size=200, verbose=2)

print("The model has successfully trained")
# Save the model
model.save("CNN_model_Digits")
print("The model has successfully saved !!")
model.summary()  # print model

# Evaluate the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("CNN error: %.2f%%" % (100 - scores[1] * 100))
