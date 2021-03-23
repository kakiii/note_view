from flask import Flask, render_template, json, jsonify, request, redirect, url_for, session
from flask_pymongo import PyMongo

app = Flask(__name__, static_folder="../dist/static", template_folder="../dist")

# 实际部署时需要更改
#数据库的文件在account.json里面
app.config["MONGO_URI"] = "mongodb://localhost:27017/account"

mongo = PyMongo(app)
database = mongo.db


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/weather')
def weather():
    with open("../dist/weather.json") as f:
        jsonStr = json.load(f)
        return json.dumps(jsonStr)


@app.route('/auth/login', methods=['POST'])
def login():
    users = mongo.db.account
    print("Connected\n")
    login_user = users.find_one({'username': request.form['username']})

    if login_user:
        print("Found one")
        # if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
        if request.form['password'] == login_user['password']:
            session['username'] = request.form['username']
            print("Check complete")
            return redirect(url_for('index'))
        else:
            print("EXISTS")
            print(request.form['password'])
            print("\n\n")
            print(login_user['password'])
            return jsonify({'status': 'exists'})
    else:
        return jsonify({'status': 'failure', 'user': request.form['username']})


if __name__ == "__main__":
    # 确保传输安全的密钥，可以随意更换
    app.secret_key = 'testing'
    app.run()
