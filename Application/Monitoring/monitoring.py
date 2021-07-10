from kafka import KafkaConsumer
import json
import beepy
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


class oxygen():
    pass


class fire():
    pass


if __name__ == "__main__":
    while 1 == 1:
        temp = Temperature()
        elec = Electrial()
        
        t1 = Thread(target=temp.monitor_temperature())
        t2 = Thread(elec.monitor_electrical())
        t1.start()
        t2.start()