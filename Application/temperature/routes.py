"""
Temperature
"""
from flask import render_template, Response, redirect, request, url_for
from Application.temperature import bp
import itertools
import time
from kafka import KafkaConsumer
import json


consumer = KafkaConsumer('temperature', bootstrap_servers=['127.0.0.1:9092'])


@bp.route('/temperature', methods=['GET', 'POST'])
def temperature1():
    if request.headers.get('accept') == 'text/event-stream':
        def events():
            for msg in consumer:
                val = json.loads(msg.value)
                yield "data: %d\n\n" % (val["payload"]["Temperature"])
                # time.sleep(.1)  # an artificial delay
        return Response(events(), content_type='text/event-stream')
    redirect('/temperature')
    return render_template('temperature.html')


@bp.route('/temperature/<value>', methods=['GET', 'POST'])
def temperature2(value):
    return "Temperature is: "+value
