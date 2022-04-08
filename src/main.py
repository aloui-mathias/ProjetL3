from cell import Cell
from floor import Floor
from maze import Maze
from fusion import Fusion
from converter import Converter

maze = Maze(cube=3)
fusion = Fusion()
fusion.generateMaze(maze)
maze.print()
list = Converter.mazeToMatrix(maze)
print("Matrice 1er étage top")
print(list[0][0])

print(maze.getCoordHoles())
