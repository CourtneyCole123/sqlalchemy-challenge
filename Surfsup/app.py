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
        f"/api/v1.0/tobs"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of precipitation for the last 12 months"""
    # Query measurement
    precip = session.query(measurement.date,measurement.prcp).filter(measurement.date >= '2016-08-23').all()
    all_precip = []
    for date, prcp in precip:
        precip_dict = {}
        precip_dict[date] = prcp
        all_precip.append(precip_dict)

    session.close()

    return jsonify(all_precip)
    json_string = json.dumps(precip_dict, default=str)

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









if __name__ == "__main__":
    app.run(debug=True)