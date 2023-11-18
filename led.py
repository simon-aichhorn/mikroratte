import sys
sys.path.append('../Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
import time
from Led import Led
from rpi_ws281x import *

class LED:
    def __init__(self):
        self.led=Led()
    
    def colorAllLeds(self):
        self.led.strip.setPixelColor(1, Color(255,0,0))
        self.led.strip.show()
    
    # cycles colors one time
    def showRainbow(self):
        self.led.rainbow(self.led.strip)
