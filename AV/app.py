from flask import Flask, render_template, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import sqlite3 as sql
import pandas as pd
from sqlalchemy import create_engine
import stock_data

#from flask_pymongo import PyMongo
#import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import MinMaxScaler
# from keras.models import Sequential, load_model
# from keras.layers import LSTM, Dense, Dropout
# import os
# import tensorflow as tf
# import yfinance as yf

#################################################
# Database Setup
#################################################
engine = create_engine("postgres://awjexunwcgwkzw:b65d9ab54cd23590803ce1b10852226b51e712eb9b8c8a9c8693dba7bd95c17e@ec2-52-1-95-247.compute-1.amazonaws.com:5432/dahtm9irpp36hu")
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://awjexunwcgwkzw:b65d9ab54cd23590803ce1b10852226b51e712eb9b8c8a9c8693dba7bd95c17e@ec2-52-1-95-247.compute-1.amazonaws.com:5432/dahtm9irpp36hu"

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
#Measurement = Base.classes.measurement
#Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



@app.route('/')
def index():
  return render_template("index.html")


if(__name__ == '__main__'):
    app.run(debug=True)
