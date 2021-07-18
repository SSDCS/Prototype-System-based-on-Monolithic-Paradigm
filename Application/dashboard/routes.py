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

# Scheduler to copy the historical sensor data to Eng.
prevData=[]
currentData=[]
def copy_to_eng():
""" # functions that copy data from the health table to engineering table
      
     Varables healthDB:
              Fire,electrical,oxygen,temp
              
     Varables EngDB:
              Fire2,electrical2,oxygen2,temp2

      TODO: Start the scheduler.
        :param bool paused: if True, don't start job processing until current job is done.
         Problem is that new child process initializes and starts a new APScheduler causing the jobs to run twice.
         For further info: https://apscheduler.readthedocs.io/en/latest/userguide.html#scheduler-events
 """
    with app.app_context():
        print("Adding to engineeringDb") # this is just for a visual test
        id=db.session.query(func.max(Sensor.id)) # current information on the engineering information
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

        id=db.session.query(func.max(SensorData.id)) # information on the health db is stored on variables
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
    
        if collections.Counter(currentData) != collections.Counter(prevData): # compares the information on the health table and the eng table,all information that are new to the health table is inserted to the eng table
            sensor_data = SensorData(fire=fire, electrical=electrical, temperature=temp, oxygen=oxygen)
            db.session.add(sensor_data)
            db.session.commit()
    
        else:
         pass       
scheduler.start() #

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    user=session['myuser']

    # Trigger Schedule
    scheduler.add_job(copy_to_eng, 'interval', seconds=60)  # inserts information to the engineering table after 60 seconds // the information is from health table
    return render_template('dashboard.html', user=user)
