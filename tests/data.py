import random
import datetime


def generate_temperature():
    temperature = random.randint(18, 21)
    return {
        "id": datetime.datetime.now(),
        "temperature:": temperature
    }
