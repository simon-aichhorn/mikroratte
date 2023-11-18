import sys
sys.path.append('../Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
import time
from Led import Led

class LED:
    def __init__(self):
        self.led=Led()
    
    def show(self):
        self.led.rainbow(self.led.strip)
