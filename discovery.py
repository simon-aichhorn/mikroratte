import sys
import time
sys.path.append('Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/Server')
from drive import Drive
from led import LED
from rfw import Rfw
from rpi_ws281x import *
from cell import Cell

drive=Drive()

grid=[]

currentPosition=(0,0)
currentOrientation='RECHTS'

is_next_cell_free_thresh = 30

def setNewCurrentPosition():
    global currentPosition
    match currentOrientation:
        case 'RECHTS':
            currentPosition=(currentPosition[0] + 1, currentPosition[1])
        case 'LINKS':
            currentPosition=(currentPosition[0] - 1, currentPosition[1])
        case 'OBEN':
            currentPosition=(currentPosition[0], currentPosition[1] - 1)
        case 'UNTEN':
            currentPosition=(currentPosition[0], currentPosition[1] + 1)

def setNewCurrentRotation():
    global currentOrientation
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
    free_ways=(false, false, false) # 1. left, 2. mid, 3. right
    
    # wait for newest data to be fetched
    time.sleep(1)
    
    # check if wall in front
    if(drive.frontDistance > is_next_cell_free_thresh):
        free_ways[1]=True

    drive.slowBackward()
    time.sleep(0.2)
    drive.stop()

    # check wall right
    drive.rotateRight()
    setNewCurrentRotation()
    time.sleep(0.5)
    if(drive.frontDistance > is_next_cell_free_thresh):
        free_ways[2]=True

    # check wall left
    drive.rotateRight()
    drive.rotateRight()
    setNewCurrentRotation()
    setNewCurrentRotation()
    time.sleep(0.5)
    if(drive.frontDistance > is_next_cell_free_thresh):
        free_ways[0]=True

    drive.rotateRight()
    setNewCurrentRotation()

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
    grid[startCell.x][startCell.y]=startCell

    time.sleep(1)

    for i in range(0,6):
        # enter next cell
        drive.driveNextField()
        setNewCurrentPosition() # update position
        
        # create new cell
        newCell=Cell(currentPosition[0], currentPosition[1])

        if(i == 0):
            # only add second cell directly to start cell, because start cell does not execute a scan
            startCell.addConnectedCell(newCell)

        grid[newCell.x][newCell.y]=newCell
        startExploration(newCell)



except KeyboardInterrupt: # interupting will stop car
    drive.stop()

except Exception as e:
    print(e)
    drive.stop()