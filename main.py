import sys
sys.path.append('Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
from drive import Drive

try:
    drive=Drive()
    
    for i in range(0, 3):
        drive.driveNextField()
        
    for i in range(0, 2):
        drive.driveBackField()
    
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    drive.stop()