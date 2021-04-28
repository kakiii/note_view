from flask.globals import request
import pymongo
import datetime
from flask import Flask, jsonify,render_template,json

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
@app.route('/content/discussion',methods=['GET'])
def return_discussion_general():
    discussions = database.discussion
    counts = discussions.find().count()
    return jsonify({'discussion_size':counts})


@app.route('/content/discussion/latest',methods=['GET'])
def return_discussion_batch():
    discussions = database.discussion
    col = discussions.find().sort([('timestamp',pymongo.ASCENDING)]).limit(1)
    collects = []
    for s in col:
        collects.append(s)
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print(collects[0])
    return jsonify({'author':collects[0]['author'],'content':collects[0]['content']})


@app.route('/content/discussion',methods=["POST"])
def insert_discussion():
    discussions = database.discussion
    request_data = request.get_data()
    data_json = json.loads(request_data)
    print(data_json)
    discussions.insert_one({'author':data_json['author'],
    'timestamp':datetime.datetime.utcnow(),
    'content':data_json['content']})
    print("GET ONE")


if __name__ == "__main__":
    app.run(debug=True)
