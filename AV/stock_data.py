import numpy as np
import json
#import matplotlib.pyplot as plt
#%matplotlib inline
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout
import yfinance as yf

def stock_query(ticker):
    
    import yfinance as yf
    stock_pick = yf.Ticker(ticker)

    stock_pick.history(period='2y')

    df = msft.history(period='2y')['Open'].values
    df = df.reshape(-1,1)

    return df

def create_model(df, ticker):
    
    dataset_train = np.array(df[:int(df.shape[0]*0.8)])
    dataset_test = np.array(df[int(df.shape[0]*0.8)-50:])

    scaler = MinMaxScaler(feature_range=(0,1))
    dataset_train = scaler.fit_transform(dataset_train)

    scaler = MinMaxScaler(feature_range=(0,1))
    dataset_train = scaler.fit_transform(dataset_train)
    dataset_test = scaler.transform(dataset_test)

    def create_models(df):
        x = []
        y = []
        for i in range(50, df.shape[0]):
            x.append(df[i-50:i,0])
            y.append(df[i,0])
        x = np.array(x)
        y = np.array(y)
        return x,y

    x_train, y_train = create_my_dataset(dataset_train)
    x_test, y_test = create_my_dataset(dataset_test)

    #reshaping for LSTM
    x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1],1))
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1],1))

    tf.logging.set_verbosity(tf.logging.ERROR)
    model = Sequential()
    model.add(LSTM(units=96, return_sequences=True, input_shape=(x_train.shape[1],1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=96, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=96))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    model.compile(loss='mean_squared_error', optimizer='adam')

    if(not os.path.exists(f'{ticker}_stock_prediction_EPBS_20_64.h5')):
        model.fit(x_train, y_train, epochs=20, batch_size=64)
        model.save(f'{ticker}_stock_prediction.h5')

    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)

    y_test_scaled = scaler.inverse_transform(y_test.reshape(-1,1))

    return # predictions and ytest_scaled???


# can we split up model creation and prediction, 
# run prediction below?
#def stock_predicter(x_test):


