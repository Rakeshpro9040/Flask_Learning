import os
from flask import Flask
from flask_smorest import Api

from db import db
import models

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint


# This is known as factory pattern
def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "rest-apis-flask-teclado-openapi"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or  os.getenv("DATABASE_URL", "sqlite:///data.db")
    # fetch from db url, else fetch from env var, else fetch from sqllite
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # Its basically slows down SQLAlchemy, hence disbaled it
    db.init_app(app)
    # initialize the Flask SQLAlchemy extension, connect it to Flask app

    api = Api(app)

    # So this will create all db tables (if not exist) 
    # before the first reuqest from client is executed
    # SQLAlchemy will refer the models and create db tables accordingly
    with app.app_context():
        db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)

    return app