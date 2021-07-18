from flask import Blueprint
#create blueprint object bp
bp = Blueprint('fire', __name__)

from Application.fire import routes