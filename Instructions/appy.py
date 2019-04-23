#%matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify
#########################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station
   

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

################################################
# flask Routes
###############################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
        
        )
##########################################
#Convert the query results to a Dictionary 
#using date as the key and prcp as the value.
#Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")
def precipitation():
    """"list of rain fall by year"""
    one_year = dt.date(2011, 1, 1) - dt.timedelta(days=365)
    prcp_results = session.query( measurement.date, measurement.prcp).\
    filter(measurement.date > one_year).\
    order_by(measurement.date).all()


    all_results = []
    for date,prcp in prcp_results:
        row = {}
        row["date"] = date
        row["prcp"] = prcp
        all_results.append(row)

    return jsonify(all_results)

######################################

@app.route("/api/v1.0/stations")
def stations():
    station_all = session.query(measurement.station).all()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(station_all))

    return jsonify(all_names)

############################################################################

@app.route("/api/v1.0/tobs")
def tobs():
    """"list of temperatures by year"""
    one_year = dt.date(2011, 1, 1) - dt.timedelta(days=365)
    temp_results = session.query(measurement.date, measurement.tobs).\
    filter(measurement.date > one_year).\
    order_by(measurement.date).all()

    temp_all = []
    for date,tobs in temp_results:
        row = {}
        row["date"] = date
        row["tobs"] = tobs
        temp_all.append(row)
    
    return jsonify(temp_all)
#########################################################################
@app.route("/api/v1.0/<start>")
def trip1(start):
    one_year = start - dt.timedelta(days=365)
    calc_temps = session.query(func.min(Measurement.tobs)), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date >= one_year).filter(Measurement.date <= one_year).all()













if __name__ == "__main__":
    app.run(debug=True)