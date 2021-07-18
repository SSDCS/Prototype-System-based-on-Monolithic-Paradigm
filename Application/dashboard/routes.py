"""
Dashboard
"""
from flask import render_template
from flask.globals import session
from Application.dashboard import bp
from ..decorators import login_required
from sqlalchemy.sql.expression import func
from application import db, app
import collections 
from Application.models import Sensor, SensorData
from apscheduler.schedulers.background import BackgroundScheduler

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    user=session['myuser']
    return render_template('dashboard.html', user=user)
