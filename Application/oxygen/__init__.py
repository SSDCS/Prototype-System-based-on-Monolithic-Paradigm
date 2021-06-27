from flask import Blueprint

bp = Blueprint('engineering', __name__)

from Application.engineering import routes