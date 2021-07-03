"""
Temperature
"""
from flask import render_template, Response, redirect, request, url_for
from Application.temperature import bp
import itertools
import time
from kafka import KafkaConsumer
import json


consumer = KafkaConsumer('temperature',bootstrap_servers=['localhost:9092'])

    
        
    

#@bp.route('/')
#def show_temp():
#    return render_template('templates/temperature.html')
@bp.route('/temperature', methods=['GET', 'POST'])
def temperature1():
    if request.headers.get('accept') == 'text/event-stream':
        def events():
            for msg in consumer:
                val = json.loads(msg.value)
                yield "data: %d\n\n" % (val["temperature:"])
                #time.sleep(.1)  # an artificial delay
        return Response(events(), content_type='text/event-stream')
    redirect('/temperature')
    return render_template('temperature.html')

@bp.route('/temperature/<value>', methods=['GET', 'POST'])
def temperature2(value):
    return "Temperature is: "+value
