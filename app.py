# nobel_viz.py

from flask import Flask
import pandas as pd

df_winners = pd.read_json('data/nobel_winners.json')

for name, group in df_winners.groupby('country'): 1
    group.to_json('data/winners_by_country' + name + '.json',\
                  orient='records')

app = Flask(__name__)

@app.route("/")  
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(port=8000, debug=True)  
