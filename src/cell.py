import sys
from copy import deepcopy
from dir import Dir

class Cell:

    def __init__(self, walls = [True,True], destroyable = [True,True],
                    partition = -1, reference = -1):
        self.walls = deepcopy(walls)
        self.destroyable = deepcopy(destroyable)
        self.partition = partition
        self.id = -1
        self.parent = None
        self.rank = -1

    def getPartition(self):
        return self.partition

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getParent(self):
        return self.parent

    def setParent(self, cell):
        self.parent = cell

    def getRank(self):
        return self.rank

    def setRank(self, rank):
        self.rank = rank

    def increaseRank(self):
        self.rank = self.rank + 1

    def hasWall(self, wall):
        return self.walls[wall]

    def buildWall(self, wall):
        self.walls[wall] = True

    def makeIndestructible(self, wall):
        if not self.hasWall(wall):
            return False
        self.destroyable[wall] = False
        return True

    def makeRightBorder(self):
        self.makeIndestructible(Dir.right)

    def makeBottomBorder(self):
        self.makeIndestructible(Dir.down)

    def isDestroyable(self, wall):
        return self.destroyable[wall]

    def destroyWall(self, wall):
        if self.isDestroyable(wall):
            self.walls[wall] = False
            return True
        else:
            return False

    def print(self, isHole = False):
        if self.walls[Dir.down] == True:
            if isHole:
                sys.stdout.write("⍜")
                #⍜⍜⍜
            else:
                sys.stdout.write("_")
        else:
            if isHole:
                sys.stdout.write("◯")
                #◯◯◯
            else:
                sys.stdout.write(" ")
        if self.walls[Dir.right] == True:
            sys.stdout.write("|")
        else:
            sys.stdout.write(" ")
            sys.stdout.flush()
