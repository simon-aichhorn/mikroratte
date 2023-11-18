import sys
import time
sys.path.append('Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
from drive import Drive
from led import LED
from rfw import Rfw
from rpi_ws281x import *

grid=[]

for y in range(0, 8):
    row = []
    for x in range(0, 8):
        row.append(None)
    grid.append(row)

try:
    drive=Drive()
    # drive.driveNextField()
    print(grid)


except KeyboardInterrupt: # interupting will stop car
    drive.stop()

except Exception as e:
    print(e)
    drive.stop()