import random
import datetime


def generate_temperature():
    temperature = random.randint(18, 21)
    return {
        "schema": {
            "type": "struct", "version": 1, "fields": [
                {"field": "ID", "type": "string"},
                {"field": "Temperature", "type": "int64"}
            ]},
        "payload": {
            "ID": datetime.datetime.now(),
            "Temperature": temperature,
        }
    }


if __name__ == "__main__":
    print(generate_temperature())
