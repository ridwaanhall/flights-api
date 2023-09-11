from flask import Flask, jsonify
from FlightRadar24 import FlightRadar24API

app = Flask(__name__)
fr_api = FlightRadar24API()


@app.route('/get_flights')
def get_flights():
  flights = fr_api.get_flights()
  # You can process the flights data as needed here
  return jsonify(flights)


@app.route('/get_airlines')
def get_airlines():
  airlines = fr_api.get_airlines()
  # You can process the airlines data as needed here
  return jsonify(airlines)
