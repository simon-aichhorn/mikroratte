import sys
sys.path.append('../Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
import time
from Led import Led
from rpi_ws281x import *

class LED:
    def __init__(self):
        self.led=Led()
        self.activateDayLight();
    
    def colorAllLeds(self, color):
        for ledIndex in range(0, 9):
            self.led.strip.setPixelColor(ledIndex, color)
        self.led.strip.show()
        
    def turnOff(self):
        self.colorAllLeds(Color(0,0,0))
    
    # cycles colors one time
    def showRainbow(self):
        self.led.rainbow(self.led.strip)

    def activateReverseLights(self):
        self.led.strip.setPixelColor(0, Color(255, 255, 255))
        self.led.strip.setPixelColor(3, Color(255, 255, 255))
        self.led.strip.show()
        
    def deactivateReverseLights(self):
        self.led.strip.setPixelColor(0, Color(0, 0, 0))
        self.led.strip.setPixelColor(3, Color(0, 0, 0))
        self.led.strip.show()

    def activateDayLight(self):
        self.led.strip.setPixelColor(1, Color(96, 0, 0))
        self.led.strip.setPixelColor(2, Color(96, 0, 0))
        
        self.led.strip.setPixelColor(5, Color(255, 255, 255))
        self.led.strip.setPixelColor(6, Color(255, 255, 255))
        self.led.strip.show()

