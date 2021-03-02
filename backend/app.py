from flask import Flask,render_template,json,jsonify
import os

app = Flask(__name__)

app = Flask(__name__,static_folder="../dist/static",template_folder="../dist")

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/weather')
def weather():
    with open("../dist/weather.json") as f:
        jsonStr = json.load(f)
        return json.dumps(jsonStr)