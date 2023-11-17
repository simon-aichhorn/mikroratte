import time
from Motor import Motor

class Drive:
    def __init__(self):
        self.motor=Motor()
        
    def stop():
        self.motor.setMotorModel(0,0,0,0)
        
    def rotateLeft():
        self.motor.setMotorModel(0,0,1500,1500)
        time.sleep(0.5)
        self.stop()