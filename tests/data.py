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


def generate_electrical():
    kilowatt = random.randint(1000, 10003)
    return {
        "schema": {
            "type": "struct", "version": 1, "fields": [
                {"field": "ID", "type": "string"},
                {"field": "Kilowatt", "type": "int64"}
            ]},
        "payload": {
            "ID": datetime.datetime.now(),
            "Kilowatt": kilowatt,
        }
    }


def generate_oxygen():
    oxygen = random.randint(75, 100)
    return {
        "schema": {
            "type": "struct", "version": 1, "fields": [
                {"field": "ID", "type": "string"},
                {"field": "O2", "type": "int64"}
            ]},
        "payload": {
            "ID": datetime.datetime.now(),
            "O2": oxygen,
        }
    }


if __name__ == "__main__":
    print(generate_temperature())
    print(generate_electrical())
    print(generate_oxygen)
