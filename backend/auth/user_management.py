import bcrypt
import pymongo
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


@auth.route('/register', methods=['POST', 'GET'])
def register():
    request_data = request.get_data()
    data_json = json.loads(request_data)

    if request.method == 'POST':
        users = database.account
        existing_user = users.find_one({'username': data_json['username']})

        if existing_user is None:
            hashes = bcrypt.hashpw(data_json['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'username': data_json['username'], 'password': hashes})
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
    print(send_out_users[0])
    jsonString = json.dumps(send_out_users)
    return jsonString