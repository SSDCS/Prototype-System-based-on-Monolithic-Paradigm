from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from argon2 import PasswordHasher
from config import Config


db = SQLAlchemy()  # instantiates the SQLAlchemy object
 # instantiates the SQLAlchemy object
ph = PasswordHasher() # instantiate the argon2 password hashinng algorithm


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    from Application.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from Application.dashboard import bp as dashboard_bp
    app.register_blueprint(dashboard_bp)

    from Application.temperature import bp as temperature_bp
    app.register_blueprint(temperature_bp)

    return app

from Application import models
