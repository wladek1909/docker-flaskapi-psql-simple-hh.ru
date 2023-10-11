from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 30 * 1024 * 1024
    app.config["CLIENT_IMAGES"] = "files"
    app.config['SECRET_KEY'] = 'qqwweerrtt1113435'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@postgres/db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_AS_ASCII'] = False
    app.config['JSON_SORT_KEYS'] = False
    db.init_app(app)

    return app
