from kafka import KafkaProducer
import json
from data import generate_temperature
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


temperature_producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    while 1 == 1:
        temperature = generate_temperature()
        print(temperature)
        temperature_producer.send("temperature", temperature)
        time.sleep(1)
