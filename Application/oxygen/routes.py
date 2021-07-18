"""
    Routes for oxygen endpoint
"""
import json
from flask import render_template, Response, redirect, request
from Application.oxygen import bp
from kafka import KafkaConsumer

#getting consumer of oxygen topic from kafka producer
consumer = KafkaConsumer('oxygen', bootstrap_servers=['127.0.0.1:9092'])

@bp.route('/oxygen', methods=['GET', 'POST'])
def oxygen1():
    """
        Function which is executed when server gets request for /oxygen endpoint
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
                yield "data: %d\n\n" % (val["payload"]["O2"])
        return Response(events(), content_type='text/event-stream')
    #refreshing /oxygen endpoint for continously displaying changing data
    redirect('/oxygen')
    #rendering oxygen.html template
    return render_template('oxygen.html')
