import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout
import os
import tensorflow as tf

# import yfinance, get MFST ticker
import yfinance as yf

tickerStr = "MFST"
ticker = yf.Ticker(tickerStr)
df = ticker.history(period='5y')['Close'].values
df = df.reshape(-1, 1)

# split 80% into training, remaining 20% + 50 values into testing data
dataset_train = np.array(df[:int(df.shape[0]*0.8)])
dataset_test = np.array(df[int(df.shape[0]*0.8)-50:])

# scale datasets
scaler = MinMaxScaler(feature_range=(0, 1))
dataset_train = scaler.fit_transform(dataset_train)
dataset_test = scaler.transform(dataset_test)

# helper function, creates batches of 50 days of stock prices
def create_my_dataset(df):
    x = []
    y = []
    for i in range(50, df.shape[0]):
        x.append(df[i-50:i, 0])
        y.append(df[i, 0])
    x = np.array(x)
    y = np.array(y)
    return x, y


x_train, y_train = create_my_dataset(dataset_train)
x_test, y_test = create_my_dataset(dataset_test)

# reshaping for LSTM
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# creating model
tf.logging.set_verbosity(tf.logging.ERROR)
model = Sequential()
model.add(LSTM(units=96, return_sequences=True, input_shape=(x_train.shape[1],1)))
model.add(LSTM(units=96, return_sequences=True))
model.add(LSTM(units=96))
model.add(Dense(units=1))

model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x_train, y_train, epochs=50, batch_size=32)
model.save(os.join("..","models",f"{tickerStr}.h5"))