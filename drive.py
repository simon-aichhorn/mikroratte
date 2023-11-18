import sys
sys.path.append('../Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
import time
from Motor import Motor
from Ultrasonic import Ultrasonic
from Buzzer import *
from servo import Servo
from rfw import Rfw
import threading

class Drive:
    def __init__(self):
        self.motor=Motor()
        self.buzzer=Buzzer()
        self.ultrasonic=Ultrasonic()
        self.initIR()
        self.pwm_S=Servo()
        self.rfw=Rfw()
        
    def initIR(self):
        self.IR01 = 14
        self.IR02 = 15
        self.IR03 = 23
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IR01,GPIO.IN)
        GPIO.setup(self.IR02,GPIO.IN)
        GPIO.setup(self.IR03,GPIO.IN)
        
    def slowForward(self, distances):
        wallDifference = distances[0] - distances[2] # positive difference = correct to left | negative difference = correct to right
        factor = 17

        nV = 750
        LW = nV - (wallDifference * factor)
        RW = nV + (wallDifference * factor)

        print(LW, RW)
        self.motor.setMotorModel(LW,LW,RW,RW)

        
    def slowBackward(self):
        self.rfw.startRFW()
        self.motor.setMotorModel(-750,-750,-750,-750)


    def stop(self):
        self.rfw.stopRFW()
        self.motor.setMotorModel(0,0,0,0)
        
    def driveNextField(self):
        while(not self.isOnLine()):
            distances=self.checkDistances()

            # check if we are standing in front of a wall
            if(distances[1] < 8):
                break

            self.slowForward(distances)
            time.sleep(0.5)
            self.stop()
        
    def driveBackField(self):
        self.slowBackward()
        
        #some sleep to drive away from line
        time.sleep(0.5)
        
        self.waitForLine()
        
    def isOnLine(self):
        return self.getIRState() == 7

    def rotateRight(self):
        self.motor.setMotorModel(1500,1500,-1500,-1500)
        time.sleep(0.725)
        self.motor.setMotorModel(0,0,0,0)
        
        
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

    def checkDistances(self):
        distances=(0,0,0)

        #read left
        self.pwm_S.setServoPWM('0', 0)
        time.sleep(0.2)
        distances=(self.ultrasonic.get_distance(), 0, 0)

        #read mid
        self.pwm_S.setServoPWM('0', 90)
        time.sleep(0.2)
        distances=(distances[0], self.ultrasonic.get_distance(), 0)

        #read right
        self.pwm_S.setServoPWM('0', 180)
        time.sleep(0.2)
        distances=(distances[0], distances[1], self.ultrasonic.get_distance())

        return checkDistances