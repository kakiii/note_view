from flask.globals import request
import pymongo
import datetime
from flask import Flask, jsonify, render_template, json

from auth.user_management import auth
from content.article import article
from content.discussion import discussion

app = Flask(__name__, static_folder="../dist/static",
            template_folder="../dist")
app.secret_key = 'testing'

client = pymongo.MongoClient(
    "mongodb+srv://zhongyiyu:Zhongyiyu123!@note-view.cfr3m.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

database = client.account

app.register_blueprint(article)
app.register_blueprint(auth)
app.register_blueprint(discussion)


@app.route('/')
def index():
    # return "<h1>SUCCESS</h1>"
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)