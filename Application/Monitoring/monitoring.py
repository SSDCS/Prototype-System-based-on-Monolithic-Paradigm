from kafka import KafkaConsumer
import json
#import beepy
from threading import Thread

temperature_consumer = KafkaConsumer(
    'temperature', bootstrap_servers=['127.0.0.1:9092'])
electrical_consumer = KafkaConsumer(
    'electrical', bootstrap_servers=['127.0.0.1:9092'])
oxygen_consumer = KafkaConsumer('oxygen', bootstrap_servers=['127.0.0.1:9092'])
fire_consumer = KafkaConsumer('fire', bootstrap_servers=['127.0.0.1:9092'])


class Temperature():
    ALARM = False
    SILENCED = False

    def __init__(self, alarm=False, silenced=False):
        self.ALARM = alarm
        self.SILENCED = silenced

        self.monitor_temperature()

    def sound_alarm(self):
        # beepy.beep(sound=1)
        if self.SILENCED == True:
            print("Alarm Silenced")
        else:
            ALARM = True
            print("Alarm")

    def silence_alarm(self):
        self.SILENCED = True

    def reset_alarm(self):
        self.SILENCED = False
        self.ALARM = False

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
    SILENCED = False

    def __init__(self, alarm=False, silenced=False):
        self.ALARM = alarm
        self.SILENCED = silenced

        self.monitor_electrical()

    def sound_alarm(self):
        # beepy.beep(sound=1)
        if self.SILENCED == True:
            print("Alarm Silenced")
        else:
            ALARM = True
            print("Alarm")

    def silence_alarm(self):
        self.SILENCED = True

    def reset_alarm(self):
        self.SILENCED = False
        self.ALARM = False

    def monitor_electrical(self):
        for watts in electrical_consumer:
            val = json.loads(watts.value)
            print(val["payload"]["Kilowatt"])
            if val["payload"]["Kilowatt"] < 1000:
                print("Kilowatt too Low")
                self.sound_alarm()
            elif val["payload"]["Kilowatt"] > 1002:
                print("Kilowatt too High")
                self.sound_alarm()
            else:
                print("Kilowatt perfect")


class Oxygen():
    ALARM = False
    SILENCED = False

    def __init__(self, alarm=False, silenced=False):
        self.ALARM = alarm
        self.SILENCED = silenced

        self.monitor_oxygen()

    def sound_alarm(self):
        # beepy.beep(sound=1)
        if self.SILENCED == True:
            print("Alarm Silenced")
        else:
            ALARM = True
            print("Alarm")

    def silence_alarm(self):
        self.SILENCED = True

    def reset_alarm(self):
        self.SILENCED = False
        self.ALARM = False

    def monitor_oxygen(self):
        for watts in electrical_consumer:
            val = json.loads(watts.value)
            print(val["payload"]["O2"])
            if val["payload"]["O2"] < 75:
                print("O2 too Low")
                self.sound_alarm()
            elif val["payload"]["O2"] > 100:
                print("O2 too High")
                self.sound_alarm()
            else:
                print("O2 perfect")


class Fire():
    ALARM = False
    SILENCED = False

    def __init__(self, alarm=False, silenced=False):
        self.ALARM = alarm
        self.SILENCED = silenced

        self.monitor_fire()

    def sound_alarm(self):
        # beepy.beep(sound=1)
        if self.SILENCED == True:
            print("Alarm Silenced")
        else:
            ALARM = True
            print("Alarm")

    def silence_alarm(self):
        self.SILENCED = True

    def reset_alarm(self):
        self.SILENCED = False
        self.ALARM = False

    def monitor_fire(self):
        for watts in electrical_consumer:
            val = json.loads(watts.value)
            print(val["payload"]["CO2"])
            if val["payload"]["CO2"] < 400:
                print("CO2 too Low")
                self.sound_alarm()
            elif val["payload"]["CO2"] > 1000:
                print("CO2 too High")
                self.sound_alarm()
            else:
                print("CO2 perfect")


if __name__ == "__main__":
    t1 = Thread(target=Temperature)
    t2 = Thread(target=Electrial)
    t3 = Thread(target=Oxygen)
    t4 = Thread(target=Fire)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t3.setDaemon(True)
    t4.setDaemon(True)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    while True:
        pass
