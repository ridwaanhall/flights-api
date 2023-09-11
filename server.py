from flask import Flask, jsonify
from FlightRadar24 import FlightRadar24API

app = Flask(__name__)
fr_api = FlightRadar24API()


@app.route('/get_flights')
def get_flights():
  flights = fr_api.get_flights()
  return jsonify(flights)


@app.route('/get_airports')
def get_airports():
  airports = fr_api.get_airports()
  print(airports)
  return airports


@app.route('/get_airlines')
def get_airlines():
  airlines = fr_api.get_airlines()
  return jsonify(airlines)


@app.route('/get_zones')
def get_zones():
  zones = fr_api.get_zones()
  return jsonify(zones)