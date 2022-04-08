from cell import Cell
from dir import Dir
import sys

class Floor():

    def __init__(self, size, next = None):
        self.top = [[Cell() for i in range(size)] for j in range(size)]
        self.bottom = [[Cell() for i in range(size)] for j in range(size)]
        self.size = size
        self.makeBorders()
        self.setIdCells()
        self.holes = []
        self.next = next
        self.generated = False

    def getTop(self):
        return self.top

    def getBottom(self):
        return self.bottom

    def getSize(self):
        return self.size

    def getHoles(self):
        return self.holes

    def isGenerated(self):
        return self.generated

    def makeGenerated(self):
        self.generated= True

    def getNextFloor(self):
        return self.next

    def setNextFloor(self, floor):
        self.next = floor

    def getCoordHoles(self):
        return [self.computeCoord(hole) for hole in self.holes]

    def makeBorders(self):
        for numCell in range(self.size):
            self.top[self.size-1][numCell].makeBottomBorder()
            self.bottom[self.size-1][numCell].makeBottomBorder()
            self.top[numCell][self.size-1].makeRightBorder()
            self.bottom[numCell][self.size-1].makeRightBorder()

    def addHole(self, hole):
        self.holes = self.holes + [hole]

    def setIdCells(self):
        i = 0;
        for line in range(self.size):
            for column in range(self.size):
                self.top[line][column].setId(i);
                self.bottom[line][column].setId(i);
                i = i + 1;

    def computeId(self, line, column):
       return (column + (line * self.size))

    def computeCoord(self, id):
        return (id//self.size,id%self.size)

    def getCell(self,cellId, halfFloor):
        coord = self.computeCoord(cellId)
        return halfFloor[coord[0]][coord[1]]

    def cellIsLeftBorder(self, cellId):
        return cellId%self.size == 0

    def cellIsTopBorder(self, cellId):
        return cellId//self.size == 0

    def cellIsRightBorder(self, cellId):
        return cellId%self.size == self.size-1

    def cellIsBottomBorder(self, cellId):
        return cellId//self.size == self.size-1

    def getNeighbor(self, dir, cellId, halfFloor):
        if dir is Dir.right:
            if self.cellIsRightBorder(cellId):
                return None
            return self.getCell(cellId+1,halfFloor)
        if dir is Dir.down:
            if self.cellIsBottomBorder(cellId):
                return None
            return self.getCell(cellId+self.size,halfFloor)
        if dir is Dir.left:
            if self.cellIsLeftBorder(cellId):
                return None
            return self.getCell(cellId-1,halfFloor)
        if self.cellIsTopBorder(cellId):
            return None
        return self.getCell(cellId-self.size,halfFloor)

    def destroyWall(self, dir, cellId, halfFloor):
        if (dir is Dir.right) or (dir is Dir.down) :
            return self.getCell(cellId,halfFloor).destroyWall(dir)
        if dir is Dir.left:
            neighbor = self.getNeighbor(dir,cellId,halfFloor)
            if neighbor is None:
                return False
            return neighbor.destroyWall(Dir.opposite(dir))
        neighbor = self.getNeighbor(dir,cellId,halfFloor)
        if neighbor is None:
            return False
        return neighbor.destroyWall(Dir.opposite(dir))

    def cellIsHole(self,cellId):
        return cellId in (self.holes + [(self.size*self.size)//2])

    def print(self):
        space_floors =("      ")
        space_titles = space_floors + "  " * (self.size-1)
        space_titles = space_titles[1:]
        print("\10")
        sys.stdout.write("Top:")
        sys.stdout.write(space_titles)
        sys.stdout.write("Bottom:")
        print("\10")
        for num in range(self.size):
            sys.stdout.write(" _")
        sys.stdout.write(space_floors + " ")
        for num in range(self.size):
            sys.stdout.write(" _")
        print("\10")
        for numLine in range(self.size):
            sys.stdout.write("|")
            for numColumn in range(self.size):
                id = self.top[numLine][numColumn].id
                self.top[numLine][numColumn].print(self.cellIsHole(id))
            sys.stdout.write(space_floors)
            sys.stdout.write("|")
            for numColumn in range(self.size):
                id = self.bottom[numLine][numColumn].id
                self.bottom[numLine][numColumn].print(self.cellIsHole(id))
            print("\10")
