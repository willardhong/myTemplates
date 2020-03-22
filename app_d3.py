# nobel_viz.py

from flask import Flask, render_template, jsonify
import pandas as pd
import json

databar = {
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

datascat = [{'x': 1, 'y': 4}, {'x': 3, 'y': 21}, {'x': 7, 'y': 5}];

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('bootstrap_1.html')

@app.route('/barchart')
def barchart():
    return render_template('d3_example1.html', databar=databar)

@app.route('/scatter2')
def scatter2():
    return render_template('d3_scatter.html', datascat=datascat)

@app.route('/combine')
def combine():
    return render_template('d3_combine.html', databar=databar, datascat=datascat)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
