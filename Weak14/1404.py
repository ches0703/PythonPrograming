# Keras application - linear regression
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
# generate data set
X = data = np.linspace(1, 2, 50)
y = X * 4 + np.random.randn(50) * 0.3  # add noise
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(1, input_dim=1, activation='linear'))
model.compile(optimizer='sgd', loss='mse', metrics=['mse'])
model.fit(X, y, batch_size=1, epochs=20, verbose=2)
predict = model.predict(data)
plt.plot(data, predict, 'r', label="linear regression")
plt.plot(data, y, 'k.', label="training data")
# blue predict line, black dots of random data
plt.title("Linear regression with Keras")
plt.legend(loc="best")
plt.show()