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
        rightFront=1500
        rightBack=1500
        
        count=0
        while(count < 10):
            count += 1
            self.motor.setMotorModel(leftFront, leftBack, rightFront, rightBack)
            time.sleep(0.1)
            
            if(leftFront == 0):
                leftFront=-1500
                leftBack=-1500
                rightFront=0
                rightBack=0
            else:
                leftFront=0
                leftBack=0
                rightFront=1500
                rightBack=1500
            
        self.stop()