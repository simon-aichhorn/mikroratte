

class Dijkstra:
    def __init__(self, grid):
        self.grid = grid
        self.waiting=[]

    def fastestWay(self, startPos):
        startCell = self.grid[startPos[0]][startPos[1]]
        startCell.cost = 0
        self.waiting.append(startCell)

    def solve(self):
        currentItem = min(self.waiting, key=lambda x: x.cost)

        for neighbor in currentItem.connectedTo.items():
            print(neighbor)

