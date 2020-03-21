# nobel_viz.py

from flask import Flask, render_template, jsonify
import pandas as pd


df_winners = pd.read_json('data/nobel_winners.json')

for name, group in df_winners.groupby('category'):
    group.to_json('data/winners_by_category' + name + '.json',\
                  orient='records')

app = Flask(__name__)

winners = [
    {'name': 'Albert Einstein', 'category':'Physics'},
    {'name': 'V.S. Naipaul', 'category':'Literature'},
    {'name': 'Dorothy Hodgkin', 'category':'Chemistry'}
]

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/demolist')
def demo_list():
    return render_template('testj2.html',
                           heading="A little winners'  list",
                           winners=jsonify(winners)
                           )

if __name__ == "__main__":
    app.run(port=8000, debug=True)
