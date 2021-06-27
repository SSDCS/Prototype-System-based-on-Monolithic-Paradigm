"""
Dashboard
"""
from flask import render_template
from Application.dashboard import bp
from ..decorators import login_required


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('dashboard.html')
