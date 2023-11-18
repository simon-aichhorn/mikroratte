import sys
sys.path.append('../Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
import time
from Buzzer import *
from Led import LED

class Rfw:
    def __init__(self):
        self.buzzer = Buzzer()
        self.led = LED()
        self.isRFWActive = False

    def activateRFW(self):
        self.isRFWActive = True
        self.buzzer_thread = threading.Thread(target=self._beep_continuously)
        self.buzzer_thread.start()
        self.led.activateReverseLights()

    def deactivateRFW(self):
        self.isRFWActive = False
        self.led.deactivateReverseLights()

    def startRFW(self):
        if not self.isRFWActive:
            self.activateRFW()

    def stopRFW(self):
        if self.isRFWActive:
            self.deactivateRFW()

    def isRFWActive(self):
        return self.isRFWActive

    def _beep_continuously(self):
        while self.isRFWActive:
            self.buzzer.run('1')
            time.sleep(1)
            self.buzzer.run('0')
            time.sleep(1)
        else:
            print("RFW is not active")
