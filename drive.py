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

        self.still_driving=False
        self.leftDistance=0 # distance to left wall
        self.rightDistance=0 # distance to right wall
        self.frontDistance=12 # distance to front

        correctingDriveThread = threading.Thread(target = self.correctDrive)
        correctingDriveThread.start()
        
    def initIR(self):
        self.IR01 = 14
        self.IR02 = 15
        self.IR03 = 23
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IR01,GPIO.IN)
        GPIO.setup(self.IR02,GPIO.IN)
        GPIO.setup(self.IR03,GPIO.IN)
        
    def slowForward(self):
        while not self.stop_driving.is_set():
            wallDifference = self.leftDistance - self.rightDistance # positive difference = correct to left | negative difference = correct to right
            factor = 12

            nV = 750
            LW = nV - (wallDifference * factor)
            RW = nV + (wallDifference * factor)

            self.motor.setMotorModel(LW,LW,RW,RW)
            time.sleep(0.25)
            self.motor.setMotorModel(0,0,0,0)
            time.sleep(0.1)

            if(self.frontDistance < 12):
                self.stop_driving.set()
        
    def slowBackward(self):
        self.rfw.startRFW()
        self.motor.setMotorModel(-750,-750,-750,-750)


    def stop(self):
        self.rfw.stopRFW()
        self.motor.setMotorModel(0,0,0,0)
        
    def driveNextField(self):
        # create stopping event
        self.stop_driving = threading.Event()

        # create forwarding driving thread
        driveForwardThread = threading.Thread(target= self.slowForward)
        
        driveForwardThread.start()

        #some sleep to drive away from line
        time.sleep(0.5)
        
        self.waitForLine()

        # stop threads
        self.stop_driving.set()
        
    def driveBackField(self):
        self.slowBackward()
        
        #some sleep to drive away from line
        time.sleep(0.5)
        
        self.waitForLine()
        
    def waitForLine(self):
        allActive = False
        # check if all ir are active
        while(not allActive):
            if(self.getIRState() == 7):
                allActive = True
        
        print("Found line!")
        self.stop()

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

    def correctDrive(self):

        while(True):
            for i in range(90,30,-60):
                self.pwm_S.setServoPwm('0',i)
                time.sleep(0.1)
                if i==30:
                    self.leftDistance = self.ultrasonic.get_distance() % 33
                elif i==90:
                    test = self.ultrasonic.get_distance()
                    self.frontDistance = test
                else:
                    self.rightDistance = self.ultrasonic.get_distance()  % 33
            for i in range(0,181,90):
                self.pwm_S.setServoPwm('0',i)
                time.sleep(0.1)
                if i==0:
                    self.leftDistance = self.ultrasonic.get_distance() % 33
                elif i==90:
                    test = self.ultrasonic.get_distance()
                    self.frontDistance = test
                else:
                    self.rightDistance = self.ultrasonic.get_distance() % 33
