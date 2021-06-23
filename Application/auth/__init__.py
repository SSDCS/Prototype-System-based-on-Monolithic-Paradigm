from flask import Blueprint

bp = Blueprint('auth', __name__, static_folder="static", template_folder="templates")

from Application.auth import routes