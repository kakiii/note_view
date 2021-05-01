import pymongo
from flask import Blueprint, jsonify, request, json

client = pymongo.MongoClient(
    "mongodb+srv://zhongyiyu:Zhongyiyu123!@note-view.cfr3m.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
database = client.account

article = Blueprint('article', __name__, url_prefix='/article')


@article.route('/<string:article_id>', methods=['GET'])
def return_article(article_id):
    article_table = database.articles
    match_article = article_table.find_one({'id': article_id})
    if match_article:
        return jsonify({'ID': article_id, 'Content': match_article['content'],'Title':match_article['title'],"author":match_article['author']})
    else:
        return jsonify(({'ID': article_id, 'Content': 'NOT FOUND'}))


@article.route('', methods=['POST'])
def add_article():
    incoming_data = request.get_data()
    jsonified_incoming_data = json.loads(incoming_data)
    returning_article_ids_arr = []
    article_table = database.articles
    article_table.insert_one({'id': jsonified_incoming_data['id'], 'content': jsonified_incoming_data['content'],'author':jsonified_incoming_data["author"],'title':jsonified_incoming_data["title"]})
    account_table = database.account
    matched_user = account_table.find_one({"username":jsonified_incoming_data['author']})
    original_article_ids = matched_user['my_article']
    original_article_titles = matched_user['article_titles']
    print(original_article_ids)
    returning_article_titles_arr = original_article_titles
    returning_article_titles_arr.append(jsonified_incoming_data['title'])
    returning_article_ids_arr = original_article_ids
    returning_article_ids_arr.append(jsonified_incoming_data['id'])
    print(returning_article_ids_arr)
    account_table.update_one({"username":jsonified_incoming_data['author']},{"$set":{"my_article":returning_article_ids_arr,"article_titles":returning_article_titles_arr}})
    return jsonify({"success":"yes"})


# Whole path should be "/article/user/<user_name>"
# An example may be "/article/user/admin", then it will return admin's all article_id.
@article.route('/user/<string:user_name>', methods=['GET'])
def return_user_article_collection(user_name):
    account_table = database.account
    matched_user = account_table.find_one({'username': user_name})
    if matched_user:
        if matched_user['my_article']:
            return jsonify({'article_collection': matched_user['my_article'],'article_titles_collection':matched_user['article_titles']})
    else:
        # temporary patch only for backend.
        print("no such user")


@article.route("/check",methods=["GET"])
def return_article_number():
    articles_table = database.articles
    article_count = articles_table.count()
    print("articles_number" + str(article_count))
    return jsonify({'article_count':article_count})