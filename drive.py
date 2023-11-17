import sys
sys.path.append('../Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
import time
from Motor import Motor
from Ultrasonic import Ultrasonic

class Drive:
    def __init__(self):
        self.motor=Motor()
        self.ultrasonic=Ultrasonic()
        
    def stop(self):
        self.motor.setMotorModel(0,0,0,0)
        
    def rotateLeft(self):
        self.motor.setMotorModel(-1500,-1500,2000,2000)
        
        lastMean = 0 # average distance of last 5 measures
        currentMean = 0 # average distance of the current 5 measures
        
        distanceCollection=[]
        while(lastMean > currentMean):
            for x in range(0,6):
                distanceCollection.append(self.ultrasonic.get_distance())
                time.sleep(0.1)
        
        
        self.stop()