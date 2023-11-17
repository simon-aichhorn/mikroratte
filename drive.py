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
        leftFront=0
        leftBack=0
        rightFront=1000
        rightBack=1000
        
        count=0
        while(count < 10):
            count += 1
            self.motor.setMotorModel(leftFront, leftBack, rightFront, rightBack)
            time.sleep(0.5)
            
            if(leftFront == 0):
                leftFront=-1000
                leftBack=-1000
                rightFront=0
                rightBack=0
            else:
                leftFront=0
                leftBack=0
                rightFront=1000
                rightBack=1000
            
        self.stop()