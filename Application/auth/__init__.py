from flask import Blueprint

bp = Blueprint('auth', __name__)

from Application.auth import routes 

# # from my_app.forms import Login, Registration #importing forms
# # from my_app.models import Astronaut, Admin #importing models
# blueprint=Blueprint("blueprint", __name__, static_folder="static", template_folder="templates") # creating a blueprint


# # from my_app.models import Admin


