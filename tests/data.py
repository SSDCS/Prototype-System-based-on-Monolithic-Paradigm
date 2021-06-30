import random

def generate_temperature():
    temperature = random.randint(18, 21)
    return {
        "temperature:": temperature
    }


if __name__ == "__main__":
    print(generate_temperature())
