"""
Temperature
"""
import json
from flask import render_template, Response, redirect, request
from Application.temperature import bp
from kafka import KafkaConsumer

#getting consumer of temperature topic from kafka producer
consumer = KafkaConsumer('temperature', bootstrap_servers=['127.0.0.1:9092'])

@bp.route('/temperature', methods=['GET', 'POST'])
def temperature1():
    """
        Function which is executed when server gets request for /temperature endpoint
        Returns:
            Returns rendered template file 'electrical.html'
    """
    if request.headers.get('accept') == 'text/event-stream':
        def events():
            """
                Function is executed when request from Kafka consumer is accepted
                Returns:
                    event, which is consumed by javascript client in front-end of an application

            """
            for msg in consumer:
                #goes through all messages in KafkaConsumer (consumer)
                val = json.loads(msg.value)
                #getting formatted needed data to yield in the event
                yield "data: %d\n\n" % (val["payload"]["Temperature"])
        return Response(events(), content_type='text/event-stream')
    #refreshing /temperature endpoint for continously displaying changing data
    redirect('/temperature')
    #rendering temperature.html template
    return render_template('temperature.html')


@bp.route('/temperature/<value>', methods=['GET', 'POST'])
def temperature2(value):
    """
        Function which is executed when server gets request for setting /temperature endpoint
        Returns:
            Returns rendered template file 'temperature.html'
            Return false if changing of temperature failed
    """
    return "Temperature is set to: "+value
