""" Define Authentication Blueprint

The following __init__ file defines the authentication blueprint name
all while defining the static and template folders.

"""
from flask import Blueprint

bp = Blueprint('auth', __name__, static_folder="static", template_folder="templates")

from Application.auth import routes
