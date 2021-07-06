"""
This is a producer that generates a temperature
This is a new line
"""
from kafka import KafkaProducer
import json
from data import generate_temperature
import time
import datetime

def defaultconverter(o):
  if isinstance(o, datetime.datetime):
      return o.__str__()

temperature_producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'],
                         value_serializer=lambda m: json.dumps(m, default=defaultconverter).encode('ascii'))

if __name__ == "__main__":
    while 1 == 1:
        temperature = generate_temperature()
        print(temperature)
        temperature_producer.send("temperature", temperature)
        time.sleep(1)
