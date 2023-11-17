import sys
sys.path.append('../Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
import time
from Motor import Motor
from Ultrasonic import Ultrasonic
from Buzzer import *

class Drive:
    def __init__(self):
        self.motor=Motor()
        self.buzzer=Buzzer()
        self.ultrasonic=Ultrasonic()
        self.initIR()
        
    def initIR(self):
        self.IR01 = 14
        self.IR02 = 15
        self.IR03 = 23
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IR01,GPIO.IN)
        GPIO.setup(self.IR02,GPIO.IN)
        GPIO.setup(self.IR03,GPIO.IN)
        
    def slowForward(self):
        self.motor.setMotorModel(750,750,750,750)
        
    def slowBackward(self):
        self.motor.setMotorModel(-750,-750,-750,-750)
        
    def stop(self):
        self.motor.setMotorModel(0,0,0,0)
        
    def driveNextField(self):
        self.slowForward()
        
        #some sleep to drive away from line
        time.sleep(0.5)
        
        allActive = False
        # check if all ir are active
        while(not allActive):
            if(self.getIRState() == 7):
                allActive = True
        
        self.stop()

        
        
        
    def getIRState(self):
        # we use a bit-coded-value for IR-State
        # left sensor = first bit = 1
        # middle sensor second bit = 2
        # right sensor = third bit = 4
        bitcoded=0x00
        
        if GPIO.input(self.IR01)==True:
            bitcoded=(bitcoded | 1)
        if GPIO.input(self.IR02)==True:
            bitcoded=(bitcoded | 2)
        if GPIO.input(self.IR03)==True:
            bitcoded=(bitcoded | 4)
        
        return bitcoded