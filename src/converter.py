from maze import Maze
from dir import Dir
import numpy as np

class Converter():

    def halfFloorToMatrix(halfFloor, size):
        horizontalWalls = np.ndarray((size+1,size))
        verticalWalls = np.ndarray((size,size+1))

        for line in range(size):
            for column in range(size):
                horizontalWalls[line+1,column] = \
                    halfFloor[line][column].hasWall(Dir.down)
                verticalWalls[line,column+1] = \
                    halfFloor[line][column].hasWall(Dir.right)
        for coord in range(size):
            horizontalWalls[0,coord] = True
            verticalWalls[coord,0] = True

        return [verticalWalls, horizontalWalls]

    def floorToMatrix(floor):
        size = floor.getSize()
        return [Converter.halfFloorToMatrix(floor.getTop(),size),\
            Converter.halfFloorToMatrix(floor.getBottom(),size)]

    def mazeToMatrix(maze):
        list = []
        currentFloor = maze.getFirstFloor()
        while currentFloor is not None:
            list = list + [Converter.floorToMatrix(currentFloor)]
            currentFloor = currentFloor.getNextFloor()
        return list