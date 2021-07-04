from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('temperature', bootstrap_servers=['127.0.0.1:9092'])


def con():

    for msg in consumer:
        val = json.loads(msg.value)
        print(val["temperature:"])


if __name__ == '__main__':
    con()
