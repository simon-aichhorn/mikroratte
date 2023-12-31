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

def getCellFromCurrentPosition():
    print(currentPosition)
    return grid[currentPosition[0]][currentPosition[1]]

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

def getFrontPosition():
    match currentOrientation:
        case 'RECHTS':
            return (currentPosition[0] + 1, currentPosition[1])
        case 'LINKS':
            return (currentPosition[0] - 1, currentPosition[1])
        case 'OBEN':
            return (currentPosition[0], currentPosition[1] - 1)
        case 'UNTEN':
            return (currentPosition[0], currentPosition[1] + 1)

def getLeftPosition():
    match currentOrientation:
        case 'RECHTS':
            return (currentPosition[0], currentPosition[1] - 1)
        case 'LINKS':
            return (currentPosition[0], currentPosition[1] + 1)
        case 'OBEN':
            return (currentPosition[0] - 1, currentPosition[1])
        case 'UNTEN':
            return (currentPosition[0] + 1, currentPosition[1])
    
def getRightPosition():
    match currentOrientation:
        case 'RECHTS':
            return (currentPosition[0], currentPosition[1] + 1)
        case 'LINKS':
            return (currentPosition[0], currentPosition[1] - 1)
        case 'OBEN':
            return (currentPosition[0] + 1, currentPosition[1])
        case 'UNTEN':
            return (currentPosition[0] - 1, currentPosition[1])

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

def createAndConnectCells(free_ways, current_cell):
    if(free_ways[0]):
        leftCellPosition=getLeftPosition()
        leftCell=grid[leftCellPosition[0]][leftCellPosition[1]]
        if(leftCell == None):
            leftCell=Cell(leftCellPosition[0], leftCellPosition[1])
        current_cell.addConnectedCell(leftCell)
        leftCell.addConnectedCell(current_cell)
        grid[leftCellPosition[0]][leftCellPosition[1]]=leftCell

    if(free_ways[1]):
        frontCellPosition=getFrontPosition()
        frontCell=grid[frontCellPosition[0]][frontCellPosition[1]]
        if(frontCell == None):
            frontCell=Cell(frontCellPosition[0], frontCellPosition[1])
        current_cell.addConnectedCell(frontCell)
        frontCell.addConnectedCell(current_cell)
        grid[frontCellPosition[0]][frontCellPosition[1]]=frontCell

    if(free_ways[2]):
        rightCellPosition=getRightPosition()
        rightCell=grid[rightCellPosition[0]][rightCellPosition[1]]
        if(rightCell == None):
            rightCell=Cell(rightCellPosition[0], rightCellPosition[1])
        current_cell.addConnectedCell(rightCell)
        rightCell.addConnectedCell(current_cell)
        grid[rightCellPosition[0]][rightCellPosition[1]]=rightCell


def startExploration(currentCell):
    free_ways=(False, False, False) # 1. left, 2. mid, 3. right
    
    # wait for newest data to be fetched
    time.sleep(1)
    
    # check if wall in front
    if(drive.checkMid() > is_next_cell_free_thresh):
        free_ways=(free_ways[0], True, free_ways[2])

    drive.slowBackward()
    time.sleep(0.5)
    drive.stop()

    # check wall right
    if(drive.checkRight() > is_next_cell_free_thresh):
        free_ways=(free_ways[0], free_ways[1], True)

    # check wall left
    if(drive.checkLeft() > is_next_cell_free_thresh):
        free_ways=(True, free_ways[1], free_ways[2])

    return free_ways

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
    startCell.discovered=True
    grid[startCell.x][startCell.y]=startCell

    time.sleep(1)

    # enter next cell
    drive.driveNextField()
    setNewCurrentPosition() # update position

    secondCell=False

    while(True):
        # get or create new cell
        newCell=getCellFromCurrentPosition()
        if(newCell == None):
            newCell=Cell(currentPosition[0], currentPosition[1])

        newCell.discovered=True

        if(not secondCell):
            # only add second cell directly to start cell, because start cell does not execute a scan
            startCell.addConnectedCell(newCell)
            newCell.addConnectedCell(startCell)
            secondCell = True

        
        free_ways = startExploration(newCell)
        print(free_ways)
        createAndConnectCells(free_ways, newCell)

        grid[newCell.x][newCell.y]=newCell

        if(free_ways[1] and not grid[getFrontPosition()[0]][getFrontPosition()[1]].discovered):

            drive.driveNextField()
        elif(free_ways[0] and not grid[getLeftPosition()[0]][getLeftPosition()[1]].discovered):
            drive.rotateRight()
            drive.rotateRight()
            drive.rotateRight()
            setNewCurrentRotation()
            setNewCurrentRotation()
            setNewCurrentRotation()
            drive.driveNextField()
        elif(free_ways[2] and not grid[getRightPosition()[0]][getRightPosition()[1]].discovered):
            drive.rotateRight()
            setNewCurrentRotation()

            drive.driveNextField()

        elif(not free_ways[0] and not free_ways[1] and not free_ways[2]):
            drive.slowBackward()
            # Implement function to go one cell back
        else:
            # we have open cells?
            print("Deadend, do we have open cells?")
            break

        drive.driveNextField()
        setNewCurrentPosition()


except KeyboardInterrupt: # interupting will stop car
    drive.stop()

#except Exception as e:
#    print(e)