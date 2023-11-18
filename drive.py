import sys
sys.path.append('../Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
import time
from Motor import Motor
from Ultrasonic import Ultrasonic
from Buzzer import *
from servo import Servo
from threading import Thread

class Drive:
    def __init__(self):
        self.motor=Motor()
        self.buzzer=Buzzer()
        self.ultrasonic=Ultrasonic()
        self.initIR()
        self.pwm_S=Servo()
        
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
        correctingDriveThread = Thread(target = self.correctDrive)
        correctingDriveThread.start()

        #some sleep to drive away from line
        time.sleep(0.5)
        
        self.waitForLine(correctingDriveThread)
        
        
    def driveBackField(self):
        self.slowBackward()
        
        #some sleep to drive away from line
        time.sleep(0.5)
        
        self.waitForLine()
        
    def waitForLine(self, correctDriveThread):
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

    def correctDrive(self):
        distanceLeft = 0
        distanceRight = 0

        while(True):
            for i in range(90,30,-60):
                self.pwm_S.setServoPwm('0',i)
                time.sleep(0.1)
                if i==30:
                    distanceLeft = self.ultrasonic.get_distance()
                #elif i==90:
                #    M = self.get_distance()
                else:
                    distanceRight = self.ultrasonic.get_distance()
                print(distanceLet, distanceRight)
            for i in range(30,151,60):
                self.pwm_S.setServoPwm('0',i)
                time.sleep(0.1)
                if i==30:
                    L = self.ultrasonic.get_distance()
                #elif i==90:
                #    M = self.get_distance()
                else:
                    R = self.ultrasonic.get_distance()
                print(distanceLet, distanceRight)
