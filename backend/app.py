import bcrypt
import pymongo
from flask import Flask, json, jsonify, request, render_template

from auth.user_management import auth
from content.article import article

app = Flask(__name__, static_folder="../dist/static",
            template_folder="../dist")
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
