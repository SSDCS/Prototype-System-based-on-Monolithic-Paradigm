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

scheduler=BackgroundScheduler()

# Scheduler
prevData=[]
currentData=[]
def copy_to_eng():
    with app.app_context():
        print("Adding to engineeringDb") #test 
        id=db.session.query(func.max(Sensor.id)) 
        sensor_data=Sensor.query.filter_by(id=id)
   
        for dt in sensor_data:
            fire=dt.fire
            electrical=dt.electrical
            oxygen=dt.oxygen
            temp=dt.temperature  
            currentData.append(fire)
            currentData.append(electrical)
            currentData.append(oxygen)
            currentData.append(temp)

        id=db.session.query(func.max(SensorData.id)) 
        sensor_data2=SensorData.query.filter_by(id=id)
        for data in sensor_data2:
            fire2=data.fire
            electrical2=data.electrical
            oxygen2=data.oxygen
            temp2=data.temperature  
            prevData.append(fire2)
            prevData.append(electrical2)
            prevData.append(oxygen2)
            prevData.append(temp2)
    
        if collections.Counter(currentData) != collections.Counter(prevData):
            sensor_data = SensorData(fire=fire, electrical=electrical, temperature=temp, oxygen=oxygen)
            db.session.add(sensor_data)
            db.session.commit()
    
        else:
         pass       
scheduler.start() 

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    user=session['myuser']

    # Trigger Schedule
    scheduler.add_job(copy_to_eng, 'interval', seconds=60)
    return render_template('dashboard.html', user=user)
