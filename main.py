import sys
import time
sys.path.append('Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
from drive import Drive
from led import LED

try:
    drive=Drive()
    led=LED()
    
    led.colorAllLeds()
    #for i in range(0, 3):
    #   drive.driveNextField()
    #  time.sleep(0.5)
        
    #for i in range(0, 2):
    #    drive.driveBackField()
    #    time.sleep(0.5)
    
except KeyboardInterrupt: # interupting will stop car
    drive.stop()