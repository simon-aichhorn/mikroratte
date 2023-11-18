import sys
sys.path.append('../Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
import time
from Buzzer import *

class Rfw:
    def __init__(self):
        self.buzzer=Buzzer()
        isRFWActive = False

    def startRFW(self):
        if not isRFWActive:
            self.activateRFW()
    
    def stopRFW(self):
        if isRFWActive:
            self.deactivateRFW()
    
    def isRFWActive(self):
        return isRFWActive

    def beep(self):
        if isRFWActive:
            self.buzzer.run('1')
            time.sleep(1)
            self.buzzer.run('0')
            time.sleep(1)
        else:
            print("RFW is not active")