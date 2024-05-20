import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

import json

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///sqlalchemy-challenge/Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Identify table names
inspector = inspect(engine)
inspector.get_table_names()

measurement = Base.classes.measurement
stations = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to my climate app!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>")


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(bind=engine)

    """Return a dictionary of precipitation for the last 12 months with date as the key and precipitation as the value"""
    # Query measurement
    precip = session.query(measurement.date,measurement.prcp).filter(measurement.date >= '2016-08-23').all()
    all_precip = []
    for date, prcp in precip:
        precip_dict = {}
        precip_dict[date] = prcp
        all_precip.append(precip_dict)

    session.close()

    return jsonify(all_precip)

@app.route("/api/v1.0/stations")
def station_names():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all stations"""
    # Query all stations
    station_names = session.query(stations.station).all()
    all_stations = []
    for station in station_names:
        all_stations.append(station)

    all_stations = list(np.ravel(all_stations))
    
    session.close()

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all temperatures"""
    # Query all temperatures
    tobs_list = session.query(measurement.tobs).filter(measurement.date >= '2016-08-23').\
        filter(measurement.station == 'USC00519281').all()
    
    all_tobs = []
    for tobs in tobs_list:
        all_tobs.append(tobs)

    all_tobs = list(np.ravel(all_tobs))

    session.close()

    return jsonify(all_tobs)

@app.route("/api/v1.0/<start>")
def start(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Fetch the min,avg,max of the temperatures by grabbing path variable supplied by the user"""
    
    start_list = session.query(func.min(measurement.tobs),func.avg(measurement.tobs),\
    func.max(measurement.tobs)).filter(measurement.date >= start).all()

    start_list = list(np.ravel(start_list))

    session.close()

    return jsonify(start_list)


@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Fetch the min,avg,max of the temperatures by grabbing path variable supplied by the user"""
    
    start_end_list = session.query(func.min(measurement.tobs),func.avg(measurement.tobs),\
    func.max(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date < end).all()
    start_end = []

    for tob_min, tob_avg, tob_max in start_end_list:
        start_end_dict = {}
        start_end_dict['Min'] = tob_min
        start_end_dict['Avg'] = tob_avg
        start_end_dict['Max'] = tob_max
        start_end.append(start_end_dict)

    session.close()

    return jsonify(start_end)

if __name__ == "__main__":
    app.run(debug=True)