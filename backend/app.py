import bcrypt
import pymongo
from flask import Flask, json, jsonify, request, redirect, url_for, session
from flask_restful import Resource, Api

# from flask_pymongo import PyMongo
app = Flask(__name__, static_folder="../dist/static", template_folder="../dist")
api = Api(app)
# 实际部署时需要更改
# 数据库的文件在account.json里面

client = pymongo.MongoClient(
    "mongodb+srv://zhongyiyu:Zhongyiyu123!@note-view.cfr3m.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

database = client.account


class Book(Resource):
    def get(self, book_id):
        print(book_id)
        articles = database.articles
        match_article = articles.find_one({'id': book_id})
        if match_article:
            return jsonify({'ID': book_id, 'Content': match_article['content']})
        else:
            return jsonify(({'ID': book_id, 'Content': 'NOT FOUND'}))


api.add_resource(Book, '/book/<int:book_id>')


@app.route('/')
def index():
    # return render_template("index.html")
    return "<h1>h1</h1>"


@app.route('/weather')
def weather():
    with open("../dist/weather.json") as f:
        jsonStr = json.load(f)
        return json.dumps(jsonStr)


@app.route('/auth/login', methods=['POST'])
def login():
    print("Connected\n")
    users = database.account
    login_user = users.find_one({'username': request.form['username']})

    if login_user:
        # 有用户
        print("Found one")
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            print("Check complete")
            return jsonify({'status': 'success', 'user': login_user['username']})
        else:
            print("EXISTS")
            print(request.form['password'])
            print("\n\n")
            print(login_user['password'])
            return jsonify({'status': 'error'})
    else:
        return jsonify({'status': 'failure', 'user': request.form['username']})


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


# @app.route('/articles/<int:article_id>', methods=['GET'])

if __name__ == "__main__":
    # 确保传输安全的密钥，可以随意更换
    app.secret_key = 'testing'
    app.run(debug=True, port=5000)
