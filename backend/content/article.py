import pymongo
from flask import Blueprint, jsonify, request, json

client = pymongo.MongoClient(
    "mongodb+srv://zhongyiyu:Zhongyiyu123!@note-view.cfr3m.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
database = client.account

article = Blueprint('article', __name__, url_prefix='/article')


@article.route('/')
def articles():
    return "<h1>ARTICLE MAIN PAGE</h1>"


@article.route('/<int:article_id>', methods=['GET'])
def return_article(article_id):
    print(article_id)
    article_collection = database.articles
    match_article = article_collection.find_one({'id': article_id})
    if match_article:
        return jsonify({'ID': article_id, 'Content': match_article['content']})
    else:
        return jsonify(({'ID': article_id, 'Content': 'NOT FOUND'}))


@article.route('/', methods=['POST'])
def add_article():
    request_data = request.get_data()
    data_json = json.loads(request_data)
    article_collection = database.articles
    article_collection.insert({'id': data_json['id'], 'content': data_json['content']})
