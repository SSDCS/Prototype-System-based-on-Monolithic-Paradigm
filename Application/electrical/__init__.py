from flask import Blueprint
#create blueprint object bp
bp = Blueprint('electrical', __name__)

from Application.electrical import routes