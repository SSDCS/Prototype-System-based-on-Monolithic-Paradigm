from flask import Flask,render_template, url_for, session, request, redirect, flash, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from functools import wraps
 

from my_app.forms import Login, Registration #importing forms
from my_app.models import Astronaut, Admin #importing models
blueprint=Blueprint("blueprint", __name__, static_folder="static", template_folder="templates") # creating a blueprint


from my_app.models import Admin


