import random
from datetime import datetime


def generate_temperature():
    temperature = random.randint(18, 21)
    return {
        "id": datetime.now(),
        "Temperature": temperature
    }


if __name__ == "__main__":
    print(generate_temperature())
