from flask import Blueprint
#create blueprint object bp
bp = Blueprint('temperature', __name__)

from Application.temperature import routes
