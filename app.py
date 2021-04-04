import bcrypt
from flask import Flask, render_template, json, jsonify, request, redirect, url_for, session

import pymongo

app = Flask(__name__, static_folder="./dist/static", template_folder="./dist")
app.secret_key = 'testing'
# 实际部署时需要更改
# 数据库的文件在account.json里面

client = pymongo.MongoClient("mongodb+srv://zhongyiyu:Zhongyiyu123!@note-view.cfr3m.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

database = client.account


@app.route('/')
def index():
    return "<h1>SUCCESS</h1>"
    # return render_template("index.html")


@app.route('/weather')
def weather():
    with open("../dist/weather.json") as f:
        jsonStr = json.load(f)
        return json.dumps(jsonStr)


@app.route('/auth/login', methods=['POST'])
def login():
    print("Connected\n")
    users = database.account
    request_data = request.get_data()
    data_json = json.loads(request_data)
    login_user = users.find_one({'username': data_json['username']})
    print(login_user)

    if login_user:
        # 有用户
        print("Found one")
        if bcrypt.hashpw(data_json['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = data_json['username']
            print("Check complete")
            # code 200 stands for user located & confirmed.
            return jsonify({'status':200})
        else:
            print("EXISTS")
            print(data_json['password'])
            print("\n")
            print(login_user['password'])
            # code 201 stands for user located but not confirmed.
            return jsonify({'status': 201})
    else:
        # code 202 stands for user not located.
        return jsonify({'status': 202, 'user': data_json['username']})


@app.route('/auth/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = database.account
        existing_user = users.find_one({'username': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'username': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for("index"))


@app.route('/articles')
def articles():
    return "<h1>hoho</h1>"


@app.route('/articles/<int:article_id>', methods=['GET'])
def return_article(article_id):
    print(article_id)
    articles = database.articles
    match_article = articles.find_one({'id': article_id})
    if match_article:
        return jsonify({'ID': article_id, 'Content': match_article['content']})
    else:
        return jsonify(({'ID': article_id, 'Content': 'NOT FOUND'}))


if __name__ == "__main__":
    # 确保传输安全的密钥，可以随意更换

    app.run(debug=True)
