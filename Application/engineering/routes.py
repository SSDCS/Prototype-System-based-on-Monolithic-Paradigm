"""
    Routes for engineering part of dashboard.
    It gathers data from databases and generates
    report containing readings and alarm logs
"""
from flask import render_template
from Application.engineering import bp


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
