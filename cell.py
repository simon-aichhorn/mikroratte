class Cell:
    
    def __init__(self, y, x):
        self.x=x
        self.y=y
        self.connectedTo=[]
        self.discovered=False
        
        # werte für dijkstra
        self.cost=None
        self.previous=None

    def addConnectedCell(self, cell):
        self.connectedTo.append(cell)