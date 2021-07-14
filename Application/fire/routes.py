"""
Fire
"""
from flask import render_template, Response, redirect, request, url_for
from Application.fire import bp
import itertools
import time
from kafka import KafkaConsumer
import json


consumer = KafkaConsumer('fire', bootstrap_servers=['127.0.0.1:9092'])


@bp.route('/fire', methods=['GET', 'POST'])
def electrical1():
    if request.headers.get('accept') == 'text/event-stream':
        def events():
            for msg in consumer:
                val = json.loads(msg.value)
                yield "data: %d\n\n" % (val["payload"]["CO"])
                # time.sleep(.1)  # an artificial delay
        return Response(events(), content_type='text/event-stream')
    redirect('/fire')
    return render_template('fire.html')
