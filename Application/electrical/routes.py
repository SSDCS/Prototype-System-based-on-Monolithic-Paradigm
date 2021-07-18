"""
    Routes for electrical endpoint
"""

import json
from flask import render_template, Response, redirect, request
from Application.electrical import bp
from kafka import KafkaConsumer


#getting consumer of electrical topic from kafka producer
consumer = KafkaConsumer('electrical', bootstrap_servers=['127.0.0.1:9092'])


@bp.route('/electrical', methods=['GET', 'POST'])
def electrical1():
    """
        Function which is executed when server gets request for /electrical endpoint
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
                yield "data: %d\n\n" % (val["payload"]["Kilowatt"])
        return Response(events(), content_type='text/event-stream')
    #refreshing /electrical endpoint for continously displaying changing data
    redirect('/electrical')
    #rendering electrical.html template
    return render_template('electrical.html')
