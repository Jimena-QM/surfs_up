# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#Set up DB engine for the Flask application. create_engine() allows us to access and query SQLite DB file
engine = create_engine("sqlite:///hawaii.sqlite")
#Reflect DB into our classes
Base = automap_base()
#Reflect DB
Base.prepare(engine, reflect=True)
#Saving references to classes in a value
Measurement = Base.classes.measurement
Station = Base.classes.station
#Create a session link from Python to our DB
session = Session(engine)

#Set Up Flask
#Define Flask app
app = Flask(__name__)
#Define welcome route
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
