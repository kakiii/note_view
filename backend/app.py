import bcrypt
import pymongo
from flask import Flask, json, jsonify, request, render_template

from auth.user_management import auth
from content.article import article

app = Flask(__name__, static_folder="../dist/static", template_folder="../dist")
app.secret_key = 'testing'
# 实际部署时需要更改
# 数据库的文件在account.json里面

client = pymongo.MongoClient(
    "mongodb+srv://zhongyiyu:Zhongyiyu123!@note-view.cfr3m.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

database = client.account

app.register_blueprint(article)
app.register_blueprint(auth)


@app.route('/')
def index():
    # return "<h1>SUCCESS</h1>"
    return render_template("index.html")


# @app.route('/content/login', methods=['POST'])
# def login():
#     print("Connected\n")
#     users = database.account
#     request_data = request.get_data()
#     data_json = json.loads(request_data)
#     login_user = users.find_one({'username': data_json['username']})
#     print(login_user)
#
#     if login_user:
#         # 有用户
#         if bcrypt.hashpw(data_json['password'].encode('utf-8'), login_user['password']) == login_user['password']:
#             session['username'] = data_json['username']
#             print("Check complete")
#             # code 200 stands for user located & confirmed.
#             return jsonify({'status': 200})
#         else:
#             print(data_json['password'])
#             print("\n")
#             print(login_user['password'])
#             # code 201 stands for user located but not confirmed.
#             return jsonify({'status': 201})
#     else:
#         # code 202 stands for user not located.
#         return jsonify({'status': 202, 'user': data_json['username']})


# @app.route('/content/register', methods=['POST', 'GET'])
# def register():
#     request_data = request.get_data()
#     data_json = json.loads(request_data)
#
#     if request.method == 'POST':
#         users = database.account
#         existing_user = users.find_one({'username': data_json['username']})
#
#         if existing_user is None:
#             hashes = bcrypt.hashpw(data_json['password'].encode('utf-8'), bcrypt.gensalt())
#             users.insert_one({'username': data_json['username'], 'password': hashes})
#             # code 200 stands for user registration success.
#             return jsonify({"status": 200})
#         else:
#             # code 201 stands for username already registered.
#             # TODO take status in frontend & display proper warnings.
#             return jsonify({"status": 201})


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
    app.run(debug=True)
