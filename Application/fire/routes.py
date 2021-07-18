"""
    Routes for fire endpoint
"""
import json
from flask import render_template, Response, redirect, request
from Application.fire import bp
from kafka import KafkaConsumer

#getting consumer of fire topic from kafka producer
consumer = KafkaConsumer('fire', bootstrap_servers=['127.0.0.1:9092'])

@bp.route('/fire', methods=['GET', 'POST'])
def fire1():
    """
        Function which is executed when server gets request for /fire endpoint
        Returns:
            Returns rendered template file 'fire.html'
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
                yield "data: %d\n\n" % (val["payload"]["CO"])
        return Response(events(), content_type='text/event-stream')
    #refreshing /fire endpoint for continously displaying changing data
    redirect('/fire')
    #rendering fire.html template
    return render_template('fire.html')
