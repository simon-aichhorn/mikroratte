import sys
sys.path.append('../Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
import time
from Motor import Motor
from Ultrasonic import Ultrasonic

class Drive:
    def __init__(self):
        self.motor=Motor()
        self.ultrasonic=Ultrasonic()
        
    def meanOf(self, array):
        sum=0
        
        for i in array:
            sum += i
            
        return sum/len(array)
        
    def stop(self):
        self.motor.setMotorModel(0,0,0,0)
        
    def rotateLeft(self):
        self.motor.setMotorModel(-1500,-1500,2000,2000)
        
        switch=0
        lastMean = 0 # average distance of last 5 measures
        currentMean = 1 # average distance of the current 5 measures
        
        while(lastMean <= currentMean):
            lastMean=currentMean
            
            read = self.ultrasonic.get_distance()
            
            if(read != 0):
                currentMean = read
            print(currentMean)
            
        lastMean = 1 # average distance of last 5 measures
        currentMean = 0 # average distance of the current 5 measures
        
        self.stop()
        time.sleep(1)
        self.motor.setMotorMode(-1500,-1500,2000,2000)
        
        while(lastMean >= currentMean):
            lastMean=currentMean
            
            read = self.ultrasonic.get_distance()
            
            if(read != 0):
                currentMean = read
            print(currentMean)
            
        self.stop()
        