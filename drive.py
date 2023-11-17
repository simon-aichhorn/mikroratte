import sys
sys.path.append('../Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
import time
from Motor import Motor

class Drive:
    def __init__(self):
        self.motor=Motor()
        
    def stop(self):
        self.motor.setMotorModel(0,0,0,0)
        
    def rotateLeft(self):
        self.motor.setMotorModel(-1500,-1500,1500,1500)
        time.sleep(0.9)
        self.stop()