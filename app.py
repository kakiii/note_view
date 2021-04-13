import bcrypt
import pymongo
from flask import Flask, json, jsonify, request, session, render_template

app = Flask(__name__, static_folder="./dist/static", template_folder="./dist")
app.secret_key = 'testing'
# 实际部署时需要更改
# 数据库的文件在account.json里面

client = pymongo.MongoClient(
    "mongodb+srv://zhongyiyu:Zhongyiyu123!@note-view.cfr3m.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

database = client.account


@app.route('/')
def index():
    # return "<h1>SUCCESS</h1>"
    return render_template("index.html")


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
        if bcrypt.hashpw(data_json['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = data_json['username']
            print("Check complete")
            # code 200 stands for user located & confirmed.
            return jsonify({'status': 200})
        else:
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
    request_data = request.get_data()
    data_json = json.loads(request_data)

    if request.method == 'POST':
        users = database.account
        existing_user = users.find_one({'username': data_json['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(data_json['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'username': data_json['username'], 'password': hashpass})
            # code 200 stands for user registration success.
            return jsonify({"status": 200})
        else:
            # code 201 stands for username already registered.
            # TODO take status in frontend & display proper warnings.
            return jsonify({"status": 201})


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


@app.route('/articles', methods=['POST'])
def add_article():
    request_data = request.get_data()
    data_json = json.loads(request_data)
    article_collection = database.articles
    article_collection.insert({'id':data_json['id'],'content':data_json['content']})


@app.route('/content/discussion/<int:discussion_id>', methods=['GET'])
def return_discussion(discussion_id):
    discussions = database.discussion
    match_discussion = discussions.find_one({'id': discussion_id})
    if match_discussion:
        return jsonify(
            {'id': discussion_id, 'content': match_discussion['content'], 'author': match_discussion['author']})
    else:
        return jsonify({
            'id': discussion_id, 'content': 'NOT FOUND'
        })


if __name__ == "__main__":
    # 确保传输安全的密钥，可以随意更换

    app.run(debug=True)
