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

        self.pwm_S.setServoPwm('0', 0)
        
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

        #if we got no prober scan, just skip it
        if(wallDifference > 20 or wallDifference < 20):
            wallDifference = 0

        factor = 12

        nV = 750
        LW = nV - (wallDifference * factor)
        RW = nV + (wallDifference * factor)

        self.motor.setMotorModel(LW,LW,RW,RW)

        
    def slowBackward(self):
        self.rfw.startRFW()
        self.motor.setMotorModel(-750,-750,-750,-750)


    def stop(self):
        self.rfw.stopRFW()
        self.motor.setMotorModel(0,0,0,0)
        
    def driveNextField(self):
        run = 0

        while(True):
            distances=self.checkDistances()

            self.slowForward(distances)
            
            if(run == 0):
                time.sleep(0.3)
            else:
                if(self.isOnLineOrWall()):
                    print("Detected Line!")
                    break

            self.stop()

            run += 1
        self.stop()
        
    def driveBackField(self):
        self.slowBackward()
        
        #some sleep to drive away from line
        time.sleep(0.5)
        
        self.waitForLine()
        
    def isOnLineOrWall(self):
        until_time = time.time() + 1

        count = 0
        while(time.time() <= until_time):
            #distance = self.ultrasonic.get_distance()
            #print(distance)
            count += 1
            # or distance < 7
            if(self.getIRState() == 7):
                return True 
        print(count)
        return False

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
            right = self.checkRight()
            left = self.checkLeft()
            mid = self.checkMid()
            return (left, mid, right)


    def checkLeft(self):
        #read left
        self.pwm_S.setServoPwm('0', 0)
        time.sleep(0.2)
        self.lastServoPos=0
        return self.ultrasonic.get_distance()

    def checkMid(self):
        #read mid
        self.pwm_S.setServoPwm('0', 90)
        time.sleep(0.2)
        self.lastServoPos=90
        return self.ultrasonic.get_distance()

    def checkRight(self):
        #read right
        self.pwm_S.setServoPwm('0', 180)
        time.sleep(0.2)
        self.lastServoPos=180
        return self.ultrasonic.get_distance()