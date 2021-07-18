"""
Dashboard
"""
from flask import render_template, redirect, url_for, flash
from flask.globals import request, session
from Application.dashboard import bp
from ..decorators import login_required
from sqlalchemy.sql.expression import func
from application import db, app
import collections 
from Application.models import Sensor, SensorData
from apscheduler.schedulers.background import BackgroundScheduler

scheduler=BackgroundScheduler()

fire=50
temp=30
oxygen=20
electrical=88

temp_status=""
oxygen_status=""
electrical_status=""
fire_status=""

def check_sensors(color):
    session['color'] = color
    global fire_status
    global oxygen_status
    global electrical_status
    global temp_status

    if fire > 100:
        session['fire_status'] = "danger"
    else:
        session['fire_status'] = "normal"
    
    if electrical > 100:
        session['electrical_status'] = "danger" 
    else:
        session['electrical_status'] = "normal"
    if oxygen > 100:
        session['oxygen_status'] = "danger"
    else:
        session['oxygen_status'] = "normal"
    if temp >100:
        session['temp_status'] = "danger"
    else:
        session['temp_status'] = "normal" 
    
    temp_status=session['temp_status'] 
    oxygen_status=session['oxygen_status']
    electrical_status=session['electrical_status']
    fire_status=session['fire_status']
    
    #insert to healthDB
    health_data=Sensor(fire=fire, temperature=temp, electrical=electrical, oxygen=oxygen)
    db.session.add(health_data)
    db.session.commit()
   
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
    col="danger"
    if "set_color" in session:
        if "set_id" in session:
            id=session['set_id']
            set_color=session['set_color']
            check_sensors(set_color+"_"+str(id))
    else:
        check_sensors(col)  
    scheduler.add_job(copy_to_eng, 'interval', seconds=60)    
    return render_template('dashboard.html', user=user, fire=fire, oxygen=oxygen, electrical=electrical,
    temp=temp, electrical_status=electrical_status, fire_status=fire_status, oxygen_status=oxygen_status, temp_status=temp_status, color=session['color'])

@bp.route('/silence/<int:id>')
@login_required
def silence(id):
    session['set_id']=id
    session['set_color'] = "normal"
    flash("Alarm silenced succesfully!")
    
    return redirect(url_for('dashboard.index'))

