from flask import Blueprint

bp = Blueprint('oxygen', __name__)

from Application.oxygen import routes