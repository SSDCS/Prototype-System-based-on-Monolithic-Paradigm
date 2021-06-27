from flask import Blueprint

bp = Blueprint('fire', __name__)

from Application.fire import routes