from flask import Blueprint
#create blueprint object bp
bp = Blueprint('engineering', __name__)

from Application.engineering import routes