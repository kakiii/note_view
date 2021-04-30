import pymongo
from flask import Blueprint, jsonify, request, json

client = pymongo.MongoClient(
    "mongodb+srv://zhongyiyu:Zhongyiyu123!@note-view.cfr3m.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
database = client.account

article = Blueprint('article', __name__, url_prefix='/article')


@article.route('/<int:article_id>', methods=['GET'])
def return_article(article_id):
    print(article_id)
    article_collection = database.articles
    match_article = article_collection.find_one({'id': article_id})
    if match_article:
        return jsonify({'ID': article_id, 'Content': match_article['content']})
    else:
        return jsonify(({'ID': article_id, 'Content': 'NOT FOUND'}))


@article.route('', methods=['POST'])
def add_article():
    request_data = request.get_data()
    data_json = json.loads(request_data)
    new_article_ids = []
    article_collection = database.articles
    article_collection.insert_one({'id': data_json['id'], 'content': data_json['content'],'author':data_json["author"],'title':data_json["title"]})
    user_collection = database.account
    dedicated_user = user_collection.find_one({"username":data_json['author']})
    original_article_ids = dedicated_user['my_article']
    print(original_article_ids)
    new_article_ids = original_article_ids
    new_article_ids.append(data_json['id'])
    print(new_article_ids)
    user_collection.update_one({"username":data_json['author']},{"$set":{"my_article":new_article_ids}})
    return jsonify({"success":"yes"})


# Whole path should be "/article/user/<user_name>"
# An example may be "/article/user/admin", then it will return admin's all article_id.
@article.route('/user/<string:user_name>', methods=['GET'])
def return_user_article_collection(user_name):
    user_db = database.account
    dedicated_user = user_db.find_one({'username': user_name})
    if dedicated_user:
        if dedicated_user['my_article']:
            return jsonify({'article_collection': dedicated_user['my_article']})
    else:
        # temporary patch only for backend.
        print("no such user")


@article.route("/check",methods=["GET"])
def return_article_number():
    articles = database.articles
    article_number = articles.count()
    print("articles_number" + str(article_number))
    return jsonify({'article_number':article_number})