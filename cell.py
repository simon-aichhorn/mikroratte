class Cell:
    
    def __init__(self, x, y):
        self.x=x
        self.y=x
        self.connectedTo=[]
        self.discovered=False
        
        # werte für dijkstra
        cost=None
        previous=None

    def addConnectedCell(self, cell):
        self.connectedTo.append(cell)