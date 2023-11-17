import sys
sys.path.append('Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
from drive import Drive

try:
    drive=Drive()
    drive.driveNextField()
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    drive.stop()