import sys
import time
sys.path.append('Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
from drive import Drive
from led import LED
from rfw import Rfw
from rpi_ws281x import *

drive=Drive()

grid=[]

currentPosition=(0,0)
currentOrientation='RECHTS'

is_next_cell_free_thresh = 30

def setNewCurrentPosition():
    match currentOrientation:
        case 'RECHTS':
            currentPosition=(currentPosition[0] + 1, currentPosition[1])
        case 'LINKS':
            currentPosition=(currentPosition[0] - 1, currentPosition[1])
        case 'OBEN':
            currentPosition=(currentPosition[0], currentPosition[1] - 1)
        case 'UNTEN':
            currentPosition=(currentPosition[0], currentPosition[1] + 1)

def setNewCurrentPosition():
    match currentOrientation:
        case 'RECHTS':
            currentOrientation='UNTEN'
        case 'LINKS':
            currentOrientation='OBEN'
        case 'OBEN':
            currentOrientation='RECHTS'
        case 'UNTEN':
            currentOrientation='LINKS'

def startExploration(currentCell):
    # wait for newest data to be fetched
    time.sleep(1)
    
    # check if wall in front
    if(drive.frontDistance > is_next_cell_free_thresh):
        print("Front is free!")

    # check wall right
    drive.rotateRight()
    setNewCurrentRotation()
    time.sleep(0.5)
    if(drive.frontDistance > is_next_cell_free_thresh):
        print("Right is free!")

    # check wall left
    drive.rotateRight()
    drive.rotateRight()
    setNewCurrentPosition()
    setNewCurrentPosition()
    time.sleep(0.5)
    if(drive.frontDistance > is_next_cell_free_thresh):
        print("Left is free!")

for y in range(0, 7):
    row = []
    for x in range(0, 7):
        row.append(None)
    grid.append(row)

try:
    # get to start line
    drive.driveNextField()

    # create start cell
    startCell=Cell(currentPosition[0], currentPosition[1])

    # enter next cell
    drive.driveNextField()
    setNewCurrentPosition() # update position
    
    # create new cell
    newCell=Cell(currentPosition[0], currentPosition[1])
    # add new cell to previous cell
    startCell.addConnectedCell(newCell)

    startExploration(newCell)

    print(grid)

except KeyboardInterrupt: # interupting will stop car
    drive.stop()

except Exception as e:
    print(e)
    drive.stop()