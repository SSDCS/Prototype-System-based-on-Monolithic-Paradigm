"""
    Routes for monitoring endpoint
"""
import json
from kafka import KafkaConsumer
from threading import Thread

#setting consumers for different topics
temperature_consumer = KafkaConsumer(
    'temperature', bootstrap_servers=['127.0.0.1:9092'])
electrical_consumer = KafkaConsumer(
    'electrical', bootstrap_servers=['127.0.0.1:9092'])
oxygen_consumer = KafkaConsumer('oxygen', bootstrap_servers=['127.0.0.1:9092'])
fire_consumer = KafkaConsumer('fire', bootstrap_servers=['127.0.0.1:9092'])


class Temperature():
    """
        Class providing monitoring/alarm functionality for temperature topic

        Attributes:
            ALARM (bool): says if there is alarm triggered
            SILENCED (bool): says if alarm was silenced
    """
    ALARM = False
    SILENCED = False

    def __init__(self, alarm=False, silenced=False):
        """
            Method which initialise an object
            Args:
                alarm (bool): says if alarm is trigerred
                silenced (bool): says if alarm was silenced
        """
        self.ALARM = alarm
        self.SILENCED = silenced
        self.monitor_temperature()

    def sound_alarm(self):
        """
            Checking if alarm was silenced
            Returns:
                "Alarm Silenced" if true
                "Alarm" if false
        """
        if self.SILENCED == True:
            print("Alarm Silenced")
        else:
            ALARM = True
            print("Alarm")

    def silence_alarm(self):
        """
            Method silences an alarm
            Returns:
                Sets class attribute SILENCED to True
        """
        self.SILENCED = True

    def reset_alarm(self):
        """
            Method resets an alarm
            Returns:
                Sets class attribute SILENCED to False
                Sets class attribute ALARM to False
        """
        self.SILENCED = False
        self.ALARM = False

    def monitor_temperature(self):
        """
            Method checks the current value of the temperature
            If value is too low or to high it triggers an alarm
            Returns:
                message (text)
                execute sound_alarm() function if temp is not right
        """
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
    """
        Class providing monitoring/alarm functionality for electrical topic

        Attributes:
            ALARM (bool): says if there is alarm triggered
            SILENCED (bool): says if alarm was silenced
    """
    ALARM = False
    SILENCED = False

    def __init__(self, alarm=False, silenced=False):
        """
            Method which initialise an object
            Args:
                alarm (bool): says if alarm is trigerred
                silenced (bool): says if alarm was silenced
        """
        self.ALARM = alarm
        self.SILENCED = silenced
        self.monitor_electrical()

    def sound_alarm(self):
        """
            Checking if alarm was silenced
            Returns:
                "Alarm Silenced" if true
                "Alarm" if false
        """
        if self.SILENCED == True:
            print("Alarm Silenced")
        else:
            ALARM = True
            print("Alarm")

    def silence_alarm(self):
        """
            Method silences an alarm
            Returns:
                Sets class attribute SILENCED to True
        """
        self.SILENCED = True

    def reset_alarm(self):
        """
            Method resets an alarm
            Returns:
                Sets class attribute SILENCED to False
                Sets class attribute ALARM to False
        """
        self.SILENCED = False
        self.ALARM = False

    def monitor_electrical(self):
        """
            Method checks the current value of the electrical topic
            If value is too low or to high it triggers an alarm
            Returns:
                message (text)
                execute sound_alarm() function if temp is not right
        """
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
    """
        Class providing monitoring/alarm functionality for oxygen topic

        Attributes:
            ALARM (bool): says if there is alarm triggered
            SILENCED (bool): says if alarm was silenced
    """
    ALARM = False
    SILENCED = False

    def __init__(self, alarm=False, silenced=False):
        """
            Method which initialise an object
            Args:
                alarm (bool): says if alarm is trigerred
                silenced (bool): says if alarm was silenced
        """
        self.ALARM = alarm
        self.SILENCED = silenced
        self.monitor_oxygen()

    def sound_alarm(self):
        """
            Checking if alarm was silenced
            Returns:
                "Alarm Silenced" if true
                "Alarm" if false
        """
        if self.SILENCED == True:
            print("Alarm Silenced")
        else:
            ALARM = True
            print("Alarm")

    def silence_alarm(self):
        """
            Method silences an alarm
            Returns:
                Sets class attribute SILENCED to True
        """
        self.SILENCED = True

    def reset_alarm(self):
        """
            Method resets an alarm
            Returns:
                Sets class attribute SILENCED to False
                Sets class attribute ALARM to False
        """
        self.SILENCED = False
        self.ALARM = False

    def monitor_oxygen(self):
        """
            Method checks the current value of the O2
            If value is too low or to high it triggers an alarm
            Returns:
                message (text)
                execute sound_alarm() function if O2 level is not right
        """
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
    """
        Class providing monitoring/alarm functionality for fire topic

        Attributes:
            ALARM (bool): says if there is alarm triggered
            SILENCED (bool): says if alarm was silenced
    """
    ALARM = False
    SILENCED = False

    def __init__(self, alarm=False, silenced=False):
        """
            Method which initialise an object
            Args:
                alarm (bool): says if alarm is trigerred
                silenced (bool): says if alarm was silenced
        """
        self.ALARM = alarm
        self.SILENCED = silenced
        self.monitor_fire()

    def sound_alarm(self):
        """
            Checking if alarm was silenced
            Returns:
                "Alarm Silenced" if true
                "Alarm" if false
        """
        if self.SILENCED == True:
            print("Alarm Silenced")
        else:
            ALARM = True
            print("Alarm")

    def silence_alarm(self):
        """
            Method silences an alarm
            Returns:
                Sets class attribute SILENCED to True
        """
        self.SILENCED = True

    def reset_alarm(self):
        """
            Method resets an alarm
            Returns:
                Sets class attribute SILENCED to False
                Sets class attribute ALARM to False
        """
        self.SILENCED = False
        self.ALARM = False

    def monitor_fire(self):
        """
            Method checks the current value of the fire topic - CO2
            If value is too low or to high it triggers an alarm
            Returns:
                message (text)
                execute sound_alarm() function if CO2 level is not right
        """
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
    #creating threads for each topic (class which reads and monitor values)
    t1 = Thread(target=Temperature)
    t2 = Thread(target=Electrial)
    t3 = Thread(target=Oxygen)
    t4 = Thread(target=Fire)
    #set threats to daemons
    t1.setDaemon(True)
    t2.setDaemon(True)
    t3.setDaemon(True)
    t4.setDaemon(True)
    #starts threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    while True:
        pass
