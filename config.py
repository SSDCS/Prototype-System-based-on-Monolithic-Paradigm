import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'thisissupposedtobemysecret' #configure a secret key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db' #configure users database
    SQLALCHEMY_BINDS = {
    'healthDB':'sqlite:///healthDB.db',
    'engineering_db':'sqlite:///engineering.db'
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False