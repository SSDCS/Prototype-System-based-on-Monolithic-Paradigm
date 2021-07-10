from kafka import KafkaConsumer

temperature_consumer = KafkaConsumer(
    'temperature', bootstrap_servers=['127.0.0.1:9092'])
electrical_consumer = KafkaConsumer(
    'electrical', bootstrap_servers=['127.0.0.1:9092'])
oxygen_consumer = KafkaConsumer('oxygen', bootstrap_servers=['127.0.0.1:9092'])
fire_consumer = KafkaConsumer('fire', bootstrap_servers=['127.0.0.1:9092'])


class Temperature():
    ALARM = False

    def monitor_temperature(self):
        for temperature in temperature_consumer:
            print(temperature["payload"]["Temperature"])
            # if temperature["payload"]["Temperature"] < 19:
            #     print("Temperature too Low")
            # elif temperature["payload"]["Temperature"] > 20:
            #     print("Temperature too High")
            # else:
            #     print("Temperature perfect")


class Electrial():
    pass


class oxygen():
    pass


class fire():
    pass


if __name__ == "__main__":
    while 1 == 1:
        temperature_monitor = Temperature()
        temperature_monitor.monitor_temperature()
