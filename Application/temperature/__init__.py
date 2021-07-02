from flask import Blueprint
bp = Blueprint('temperature', __name__)
from Application.temperature import routes



