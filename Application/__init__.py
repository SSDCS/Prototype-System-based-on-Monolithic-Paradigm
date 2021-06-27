from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from config import Config

db = SQLAlchemy()  # instantiates the SQLAlchemy object
bcrypt = Bcrypt()  # instatiate the bcrypt to help in hashing of passwords


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)

    from Application.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from Application.dashboard import bp as dashboard_bp
    app.register_blueprint(dashboard_bp)

    return app

from Application import models
