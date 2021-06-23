from flask import Blueprint

bp = Blueprint('dashboard', __name__)

from Application.dashboard import routes