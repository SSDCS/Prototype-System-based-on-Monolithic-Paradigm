from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

dashboard = Blueprint('dashboard', __name__, template_folder='templates')


@dashboard.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)