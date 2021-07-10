from kafka import KafkaConsumer
import json
import beepy

temperature_consumer = KafkaConsumer(
    'temperature', bootstrap_servers=['127.0.0.1:9092'])
electrical_consumer = KafkaConsumer(
    'electrical', bootstrap_servers=['127.0.0.1:9092'])
oxygen_consumer = KafkaConsumer('oxygen', bootstrap_servers=['127.0.0.1:9092'])
fire_consumer = KafkaConsumer('fire', bootstrap_servers=['127.0.0.1:9092'])


class Temperature():
    ALARM = False
    SILENCED = False

    def sound_alarm(self):
        # beepy.beep(sound=1)
        if self.SILENCED == True:
            print("Alarm Silenced")
        else:
            ALARM = True
            print("Alarm")

    def silence_alarm(self):
        self.SILENCED = True

    def monitor_temperature(self):
        for temperature in temperature_consumer:
            val = json.loads(temperature.value)
            print(val["payload"]["Temperature"])
            if val["payload"]["Temperature"] < 19:
                print("Temperature too Low")
                self.sound_alarm()
            elif val["payload"]["Temperature"] > 20:
                print("Temperature too High")
                self.sound_alarm()
            else:
                print("Temperature perfect")


class Electrial():
    ALARM = False
    SILENCED = True

    def sound_alarm(self):
        # beepy.beep(sound=1)
        if self.SILENCED == True:
            print("Alarm Silenced")
        else:
            ALARM = True
            print("Alarm")

    def silence_alarm(self):
        self.SILENCED = True

    def monitor_electrical(self):
        for watts in electrical_consumer:
            val = json.loads(watts.value)
            print(val["payload"]["Temperature"])
            if val["payload"]["Temperature"] < 19:
                print("Temperature too Low")
                self.sound_alarm()
            elif val["payload"]["Temperature"] > 20:
                print("Temperature too High")
                self.sound_alarm()
            else:
                print("Temperature perfect")


class oxygen():
    pass


class fire():
    pass


if __name__ == "__main__":
    while 1 == 1:
        temperature_monitor = Temperature()
        temperature_monitor.monitor_temperature()
