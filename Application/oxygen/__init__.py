from flask import Blueprint
#create blueprint object bp
bp = Blueprint('oxygen', __name__)

from Application.oxygen import routes