import pymongo
from flask import Blueprint, jsonify, request, json
import datetime

client = pymongo.MongoClient(
    "mongodb+srv://zhongyiyu:Zhongyiyu123!@note-view.cfr3m.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
database = client.account

discussion = Blueprint('discussion', __name__, url_prefix='/content/discussion')

@discussion.route('/', methods=['GET'])
def return_discussion_general():
    discussions = database.discussion
    counts = discussions.find().count()
    return jsonify({'discussion_size': counts})

@discussion.route('/latest', methods=['GET'])
def return_latest_index():
    discussions = database.discussion
    size = discussions.count()
    return jsonify({'latest':size})

@discussion.route('/', methods=["POST"])
def insert_discussion():
    request_data = request.get_data()
    discussions = database.discussion
    json_data = json.loads(request_data)
    print("\n\n\n\n\n\n\n\n\n")
    print(json_data)
    discussions.insert({
        "author":json_data["author"],
        "content":json_data["content"],
        "timestamp":datetime.datetime.utcnow(),
        "seq":discussions.find().count()+1
        })
    return 0