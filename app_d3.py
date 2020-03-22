# nobel_viz.py

from flask import Flask, render_template, jsonify
import pandas as pd
import json

data = {
  'labels': [
    'Persona 1', 'Persona 2', 'Persona 3',
    'Persona 4', 'Persona 5', 'Persona 6'
  ],
  'series': [
    {
      'label': 'Branch',
      'values': [12, 43, 22, 11, 73, 25]
    },
    {
      'label': 'US',
      'values': [31, 28, 14, 8, 15, 21]
    }]
}

datascatter = [{'x': 12, 'y': 12}, {'x': 11, 'y': 21}, {'x': 12, 'y': 5}];

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/barchart')
def barchart():
    return render_template('d3_example1.html',
                           data=data
                           )

@app.route('/scatter')
def scatter():
    return render_template('d3_example2.html',
                  data=datascatter)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
