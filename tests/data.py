import random


def generate_temperature():
    temperature = random.randint(18, 21)
    return {
        "schema": {
            "type": "struct", "optional": false, "version": 1, "fields": [
                {"field": "Temperature", "type": "int"}
            ]},
        "payload": {
            "Temperature": temperature
        }
    }


if __name__ == "__main__":
    print(generate_temperature())
