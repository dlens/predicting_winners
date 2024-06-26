import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd
import matplotlib.pyplot as plt

# unsure why I am getting red squiggles under these imports, but they still work so whatever

# import and format data
training = pd.read_excel('training2.xlsx')
testing = pd.read_excel('testing2.xlsx')

train_x = training['input']
train_y = training['output']
test_x = testing['input']
test_y = testing['output']

# Define the model
model = Sequential()
model.add(Dense(300, activation='relu'))
model.add(Dense(150, activation='relu'))
model.add(Dense(75, activation='relu'))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(train_x, train_y, epochs=60, batch_size=1, verbose=1)

# make some predictions
pred_y = model.predict(test_x)

# plot results
plt.figure(figsize=(10, 6))
plt.plot(test_x, test_y, label='True Sin')
plt.plot(test_x, pred_y, label='Predicted function')
plt.legend()
plt.show()