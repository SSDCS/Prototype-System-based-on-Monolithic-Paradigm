import random
from datetime import datetime


def generate_temperature():
    temperature = random.randint(18, 21)
    return {
        "schema": {
            "type": "struct", "version": 1, "fields": [
                {"field": "ID", "type": "int"},
                {"field": "Temperature", "type": "int"}
            ]},
        "payload": {
            "ID": datetime.now(),
            "Temperature": temperature,
        }
    }


if __name__ == "__main__":
    print(generate_temperature())
