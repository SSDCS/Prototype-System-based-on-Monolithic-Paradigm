"""
This is a producer that generates a temperature
This is a new line
"""
from tests.data import generate_electrical, generate_fire, generate_oxygen
from kafka import KafkaProducer
import json
from tests.data import generate_temperature, generate_electrical, generate_fire, generate_oxygen
import time
import datetime


def default(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()


temperature_producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'],
                                     value_serializer=lambda m: json.dumps(m, default=default).encode('ascii'))

electrical_producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'],
                                    value_serializer=lambda m: json.dumps(m, default=default).encode('ascii'))


oxygen_producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'],
                                value_serializer=lambda m: json.dumps(m, default=default).encode('ascii'))


fire_producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'],
                              value_serializer=lambda m: json.dumps(m, default=default).encode('ascii'))

if __name__ == "__main__":
    while 1 == 1:
        temperature = generate_temperature()
        electrical = generate_electrical()
        oxygen = generate_oxygen()
        fire = generate_fire()
        print(temperature)
        print(electrical)
        print(oxygen)
        print(fire)
        temperature_producer.send("temperature", temperature)
        electrical_producer.send("temperature", electrical)
        oxygen_producer.send("temperature", oxygen)
        fire_producer.send("temperature", fire)
        time.sleep(1)
