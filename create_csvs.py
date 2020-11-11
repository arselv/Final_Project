import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
import os
import yfinance as yf

def make_csvs():
  tickers = ["AAPL","AMZN","GOOG","MSFT","TLSA"]

  for tickerStr in tickers:

    model = load_model(os.path.join("static","models",f"{tickerStr}.h5"))

    ticker = yf.Ticker(tickerStr)
    df = ticker.history(period='5y')['Close'].values
    df = df.reshape(-1, 1)
    dataset_train = np.array(df[:int(df.shape[0]*0.8)])
    dataset_test = np.array(df[int(df.shape[0]*0.8)-50:])
    scaler = MinMaxScaler(feature_range=(0,1))
    dataset_train = scaler.fit_transform(dataset_train)
    dataset_test = scaler.transform(dataset_test)

    def create_my_dataset(df):
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

    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)

    predictions_prepended = [0 for i in range(0,df.shape[0]-len(predictions))]
    predictions_prepended.extend(predictions.flatten().tolist())

    overall = pd.DataFrame({
        "closing_prices": df.flatten().tolist(),
        "predicted_prices": predictions_prepended,
    })
    overall.to_csv(os.path.join("static","data",f"{tickerStr}_overall.csv"),index_label="Index")

    y_test_scaled = scaler.inverse_transform(y_test.reshape(-1,1))
    y_test_zoomed = y_test_scaled.flatten().tolist()
    zoomed = pd.DataFrame({
        "closing_prices": y_test_scaled.flatten().tolist(),
        "predicted_prices": predictions.flatten().tolist()
    })
    zoomed.to_csv(os.path.join("static","data",f"{tickerStr}_zoomed.csv"),index_label="Index")