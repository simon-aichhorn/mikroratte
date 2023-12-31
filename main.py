import sys
import time
sys.path.append('Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
from drive import Drive
from led import LED
from rfw import Rfw
from rpi_ws281x import *

try:
    drive=Drive()
    led=LED()
    rfw=Rfw()
    
    # led.activateReverseLights()
    # time.sleep(2)
    
    # led.deactivateReverseLights()

    # time.sleep(2)
    # led.turnOff()

    # time.sleep(2)
    # led.blinkers('left')

    # time.sleep(2)
    # led.turnOff()
    # led.blinkers('right')

    # time.sleep(2)
    # led.turnOff()
    # led.blinkers('hazard')

    # time.sleep(2)
    # led.turnOff()
    # drive.driveNextField()
    # time.sleep(2)
    # drive.driveNextField()
    # time.sleep(2)
    # drive.driveNextField()
    drive.slowBackward()
    time.sleep(2)
    drive.stop()




except KeyboardInterrupt: # interupting will stop car
    drive.stop()

except Exception as e:
    print(e)
    drive.stop()
    led.turnOff()
    led.blinkers('hazard')