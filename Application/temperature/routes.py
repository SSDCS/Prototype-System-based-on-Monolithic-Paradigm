"""
Temperature
"""
from flask import render_template
from Application.temperature import bp
from kafka import KafkaConsumer
import json

def con():
    consumer = KafkaConsumer('temperature',bootstrap_servers=['localhost:9092'])

    for msg in consumer:
        val = json.loads(msg.value)
        print(val["temperature:"])

#@bp.route('/')
#def show_temp():
#    return render_template('templates/temperature.html')
@bp.route('/temperature', methods=['GET', 'POST'])
def temperature1():
    return render_template('temperature.html')

@bp.route('/temperature/<value>', methods=['GET', 'POST'])
def temperature2(value):
    return "Temperature is: "+value
