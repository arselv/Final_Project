from flask import Flask, render_template, jsonify
from static.py import create_csvs
from static.py import api

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/create-csvs')
def create():
  create_csvs.make_csvs()
  return "created csvs successfully"

@app.route('/api/<tickerStr>')
def api_route(tickerStr):
  return jsonify(api.return_json(tickerStr))


if(__name__ == '__main__'):
    app.run(debug=True)
