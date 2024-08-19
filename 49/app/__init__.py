from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

mongo = PyMongo()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/my_flask_app"
    app.config['SECRET_KEY'] = 'supersecretkey'

    mongo.init_app(app)
    bcrypt.init_app(app)

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
