from flask import Blueprint

bp = Blueprint('electrical', __name__)

from Application.electrical import routes