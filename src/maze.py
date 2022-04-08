import sys

from floor import Floor

class Maze():

    def __init__(self, size = 0, height = 0, cube = 0):
        if ((size is 0 and height is 0 and cube is 0) or
                (size is not 0 and height is 0) or
                (size is 0 and height is not 0) or
                (size is not 0 and cube is not 0) or
                (height is not 0 and cube is not 0)):
            print("Erreur initialisation Maze")
            sys.exit()
        if cube is not 0:
            height = cube
            size = cube * 2 - 1
        self.firstFloor = Floor(size)
        self.height = height
        self.addFloors(height-1)
        self.generated = False

    def getFirstFloor(self):
        return self.firstFloor

    def getHeight(self):
        return self.height

    def increaseHeight(self):
        self.height = self.height + 1

    def isGenerated(self):
        return self.generated

    def makeGenerated(self):
        self.generated= True

    def getLastFloor(self):
        lastFloor = self.firstFloor
        while lastFloor.getNextFloor() is not None:
            lastFloor = lastFloor.getNextFloor()
        return lastFloor

    def addFloor(self):
        size = self.firstFloor.getSize()
        lastFloor = self.getLastFloor()
        lastFloor.setNextFloor(Floor(size))
        self.increaseHeight()
        self.generated = False

    def addFloors(self, nbFloors):
        for floor in range(nbFloors):
            self.addFloor()

    def getCoordHoles(self):
        list = []
        currentFloor = self.firstFloor
        while currentFloor is not None:
            list = list + [currentFloor.getCoordHoles()]
            currentFloor = currentFloor.getNextFloor()
        return list

    def print(self):
        currentFloor = self.firstFloor
        i = 1
        while currentFloor is not None:
            print("\nFloor " + str(i) + ":")
            currentFloor.print()
            currentFloor = currentFloor.getNextFloor()
            i = i + 1
        print()