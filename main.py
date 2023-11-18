import sys
import time
sys.path.append('Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
from drive import Drive
from led import LED
from rpi_ws281x import *

try:
    drive=Drive()
    led=LED()
    
    led.activateReverseLights()
    time.sleep(2)
    
    led.deactivateReverseLights()

    time.sleep(2)
    led.turnOff()
    
except KeyboardInterrupt: # interupting will stop car
    drive.stop()