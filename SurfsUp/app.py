# Import the dependencies.
import pandas as pd
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        "Welcome to the Honolulu, Hawaii Climate Analysis"
        "The available pages are:"
        "/api/v1.0/precipitation"
        "/api/v1.0/stations"
        "/api/v1.0/tobs"
        "/api/v1.0/<start>"
        "/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def preciptiation():
    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    last_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= last_year).all()
    precipitation_list = []
    for date, prcp in last_data:
        precipitation_dict = {}
        precipitation_dict['date'] = date
        precipitation_dict['prcp'] = prcp
        precipitation_list.append(precipitation_dict)
    return jsonify(precipitation_listt)
    
@app.route("/api/v1.0/stations")
def stations():
    station_data = session.query(Station.station).all()
    station_list = []
    for station in station_data:
        station_list.append(station)
    return jsonify(station_list)
        
@app.route("/api/v1.0/tobs")
def tobs():
    tobs_data = = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').\
                    filter(Measurement.date >= last_year).all()
    tobs_list = []
    for date, tobs in tobs_data:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_list.append(tobs_dict)
    return jsonify(tobs_list)
    
@app.route("/api/v1.0/<start>")
def StartDate():
    Results = session.query(Measurement.date, func.min(Measurement.tobs), func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date >= start_date_only).group_by(Measurement.date).all()
    start_list = []
    for date,tmin,tmax,tavg in Results:
        start_dict = {}
        start_dict['Date'] = date
        start_dict['TMIN'] = tmin
        start_dict['TMAX'] = tmax
        start_dict['TAVG'] = tavg
        start_list.append(start_dict)

    return jsonify(start_list)
    
@app.route("/api/v1.0/<start>/<end>")
Def StartEndDate():
    Results = session.query(Measurement.date, func.min(Measurement.tobs), func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date<=end_date).group_by(Measurement.date).all()
    startend_list = []
    for date,Tmin,Tmax,Tavg in Resultss:
        startend_dict = {}
        startend_dict['Date'] = date
        startend_dict['TMIN'] = Tmin
        startend_dict['TMAX'] = Tmax
        startend_dict['TAVG'] = Tavg
        startend_list.append(startend_dict)

    return jsonify(startend_list)








    
    