import bcrypt
import pymongo
import re
from flask import Blueprint, jsonify, request, json, session

client = pymongo.MongoClient(
    "mongodb+srv://zhongyiyu:Zhongyiyu123!@note-view.cfr3m.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
database = client.account

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['POST'])
def login():
    users = database.account
    request_data = request.get_data()
    data_json = json.loads(request_data)
    login_user = users.find_one({'username': data_json['username']})
    print(login_user)

    if login_user:
        # 有用户
        if bcrypt.hashpw(data_json['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = data_json['username']
            if login_user["ban"] == 100:
                return jsonify({"status": 203})
            else:
                return jsonify({'status': 200})
            # print("Check complete")
            # code 200 stands for user located & confirmed.
            
        else:
            # print(data_json['password'])
            # print("\n")
            # print(login_user['password'])
            # code 201 stands for user located but not confirmed.
            return jsonify({'status': 201})
    else:
        # code 202 stands for user not located.
        return jsonify({'status': 202, 'user': data_json['username']})


@auth.route('/register', methods=['POST', 'GET'])
def register():
    request_data = request.get_data()
    data_json = json.loads(request_data)

    if request.method == 'POST':
        users = database.account
        existing_user = users.find_one({'username': data_json['username']})

        if existing_user is None:
            hashes = bcrypt.hashpw(data_json['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'username': data_json['username'], 'password': hashes,'my_article':[],'ban':0,'article_titles':[]})
            # code 200 stands for user registration success.
            return jsonify({"status": 200})
        else:
            # code 201 stands for username already registered.
            # TODO take status in frontend & display proper warnings.
            return jsonify({"status": 201})

@auth.route('/check',methods=['GET'])
def return_user_number():
    user = database.account
    return_user_number = user.count()
    return jsonify({'user_number':return_user_number})

@auth.route('/getAllUser',methods=["GET"])
def return_all_username():
    users = database.account
    send_out_users = []
    cursor = users.find({})
    for doc in cursor:
        send_out_users.append(doc["username"])
    # print(send_out_users[0])
    jsonString = json.dumps(send_out_users)
    return jsonString

@auth.route('/findUser',methods=["POST"])
def return_certain_user():
    name_raw = request.get_data()
    name_json = json.loads(name_raw)
    name_extract = name_json["username"]
    real_name = name_extract + "*"
    users = database.account
    regex = re.compile(real_name,re.IGNORECASE)
    cursor = users.find_one({"username":regex})
    username_return = cursor["username"]
    return jsonify({
        "username":username_return
    })

@auth.route('/banUser',methods=["PUT"])
def ban_user():
    users_collection = database.account
    incoming_user_name = request.get_data()
    incoming_json = json.loads(incoming_user_name)
    real_user_name = incoming_json["username"]
    if(users_collection.find_one({"username":real_user_name})):
        dedicated_user = users_collection.find_one({"username":real_user_name})
        users_collection.update_one({"username":real_user_name},{"$set":{"ban":100}})
        print("Delete complete")
        return jsonify({"delete":"done"})
    else:
        return jsonify({"delete":"undone"})

@auth.route('/banUserList',methods=["GET"])
def return_all_ban_users():
    arr = []
    users_collection = database.account
    for x in users_collection.find({"ban":100},{"username":1}):
        arr.append(x['username'])
    json_arr = json.dumps(arr)
    return json_arr