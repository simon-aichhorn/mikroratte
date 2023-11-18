class Cell:
    
    def __init__(self, x, y):
        self.x=x
        self.y=x
        self.connectedTo=[]

    def addConnectedCell(self, cell):
        self.connectedTo.append(cell)