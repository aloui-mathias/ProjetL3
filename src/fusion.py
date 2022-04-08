import random

from maze import Maze
from floor import Floor
from cell import Cell

class Fusion(object):

    def __init__(self, hard = False):
        self.hard = hard

    def generateMaze(self, maze):
        currentFloor = maze.getFirstFloor()
        while currentFloor is not None:
            self.generateFloor(currentFloor)
            currentFloor = currentFloor.getNextFloor()
        maze.makeGenerated()

    def generateFloor(self, floor):
        if self.hard:
            self.generateFloorHard(floor)
        else:
            self.generateFloorMedium(floor)

    def generateFloorMedium(self, floor):
        self.generateHalfFloorMedium(floor.getTop(), floor)
        self.generateHalfFloorMedium(floor.getBottom(), floor)
        self.createHole(floor)
        floor.makeGenerated()

    def generateFloorHard(self, floor):
        pass

    def generateHalfFloorMedium(self, halfFloor, floor):
        self.makeSet(halfFloor,floor)
        size = floor.getSize()
        nbCells = size * size
        idCells = [i for i in range(nbCells-1)]
        for line in range(size-1):
            idCells = idCells + [(line*size + i) for i in range(size-1)]
        random.shuffle(idCells)
        for idCell in idCells:
            dir = random.randint(0,1)
            cell = floor.getCell(idCell,halfFloor)
            neighbor = floor.getNeighbor(dir,idCell,halfFloor)
            if neighbor is None:
                dir = (dir+1)%2
                neighbor = floor.getNeighbor(dir,idCell,halfFloor)
            rootCell = self.find(cell)
            rootNeighbor = self.find(neighbor)
            if rootCell is rootNeighbor:
                continue
            if floor.destroyWall(dir,idCell,halfFloor):
                self.union(cell,neighbor)

    def makeSet(self, halfFloor, floor):
        size = floor.getSize()
        nbCells = size*size
        for idCell in range(nbCells):
            cell = floor.getCell(idCell,halfFloor)
            cell.setParent(cell)
            cell.setRank(0)

    def find(self, cell):
        parent = cell.getParent()
        if parent is not cell :
            cell.setParent(self.find(parent))
        return cell.getParent()

    def union(self, cellA, cellB):
        rootA = self.find(cellA)
        rootB = self.find(cellB)
        if rootA is not rootB:
            if rootA.getRank() < rootB.getRank():
                rootA.setParent(rootB)
            else:
                rootB.setParent(rootA)
                if rootA.getRank() == rootB.getRank():
                    rootA.increaseRank()

    def getPossibleHoles(self, size):
        idCells = [i for i in range(1,size//2)]
        idCells = [i for i in range(size//2+1,size-1)]
        idCells = idCells + [i*size for i in range(size//2)]
        idCells = idCells + [i*size for i in range(size//2+1,size)]
        idCells = idCells + [size-1+i*size for i in range(size//2)]
        idCells = idCells + [size-1+i*size for i in range(size//2+1,size)]
        idCells = idCells + [size*(size-1)+i for i in range(1,size//2)]
        idCells = idCells + [size*(size-1)+i for i in range(size//2+1,size-1)]
        return idCells

    def createHole(self, floor):
        allHoles = self.getPossibleHoles(floor.getSize())
        listPossibleHoles = [x for x in allHoles if x not in floor.holes]
        hole = random.choice(listPossibleHoles)
        floor.addHole(hole)
