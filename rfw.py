import sys
sys.path.append('../Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
import time
from Buzzer import *
from Led import led

class Rfw:
    def __init__(self):
        self.buzzer=Buzzer()
        self.led=Led()
        isRFWActive = False

    def startRFW(self):
        if not isRFWActive:
            self.activateRFW()
            self.led.activateReverseLights()
    
    def stopRFW(self):
        if isRFWActive:
            self.led.deactivateReverseLights()
            self.deactivateRFW()
    
    def isRFWActive(self):
        return isRFWActive

    def beep(self):
        while isRFWActive:
            self.buzzer.run('1')
            time.sleep(1)
            self.buzzer.run('0')
            time.sleep(1)
        else:
            print("RFW is not active")