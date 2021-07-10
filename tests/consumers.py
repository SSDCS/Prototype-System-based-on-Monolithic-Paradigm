from kafka import KafkaConsumer
import json

temperature_consumer = KafkaConsumer(
    'temperature', bootstrap_servers=['127.0.0.1:9092'])
electrical_consumer = KafkaConsumer(
    'electrical', bootstrap_servers=['127.0.0.1:9092'])


def con():

    for msg in temperature_consumer:
        val = json.loads(msg.value)
        print(val["payload"]["Temperature"])


if __name__ == '__main__':
    print("consumer")
    con()
