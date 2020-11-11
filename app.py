from flask import Flask, render_template
import create_csvs

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



if(__name__ == '__main__'):
    app.run(debug=True)
