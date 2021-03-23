from flask import Flask,render_template,json,jsonify,request
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
@app.route('/auth/login',methods=['POST'])
def login():
    user_data = request.get_json()
    print(user_data)
    user = "yiyu"
    return jsonify({'status': 'success', 'user': "yiyu"})
if __name__ == "__main__":
    app.run()