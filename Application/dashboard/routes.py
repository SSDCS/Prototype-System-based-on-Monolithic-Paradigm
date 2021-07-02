"""
Dashboard
"""
from flask import render_template
from flask.globals import session
from Application.dashboard import bp
from ..decorators import login_required


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    user=session['myuser']
    return render_template('dashboard.html', user=user)
