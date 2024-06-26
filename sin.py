import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
import pandas as pd

# import data
training = pd.read_excel('training.xlsx')
testing = pd.read_excel('testing.xlsx')

train_x = training['input']
train_y = training['output']
test_x = testing['input']
test_y = testing['output']

# Define the model
model = Sequential()
model.add(Dense(50, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(train_x, train_y, epochs=5, batch_size=32, verbose=2)

