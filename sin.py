import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
import matplotlib.pyplot as plt
import pandas as pd

# import data
training = pd.read_excel('sinData.xlsx')
testing = pd.read_excel('sinTesting.xlsx')

train_x = training['input']
train_y = training['output']
test_x = testing['input']
test_y = testing['output']

# Define the model
model = Sequential()
model.add(Dense(50, input_dim=1, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(train_x, train_y, epochs=100, batch_size=32, verbose=1)

# Make predictions
pred_y = model.predict(test_x)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(test_x, test_y, label='True Function')
plt.plot(test_x, pred_y, label='Neural Network Predictions')
plt.legend()
plt.show()

