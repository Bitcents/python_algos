from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
#from generic_search import dfs, bfs, node_to_path, astar, Node

class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"


class MazeLocation(NamedTuple):
    row: int
    column: int

class Maze:
    def __init__(self, rows: int = 10, columns: int = 10, sparseness: float = 0.2, start: MazeLocation = MazeLocation(0, 0), goal: MazeLocation = MazeLocation(9, 9)) -> None:
        # basic initialization
        self._rows: int = rows
        self._columns: int = columns
        self._sparseness: float = sparseness
        self._start: MazeLocation = start
        self._goal: MazeLocation = goal
        # fill the maze with empty cells
        # using list composition to get this all in one line
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        # then we randomly fill the grid, according to the sparseness factor
        self._randomly_fill(rows, columns, sparseness)
        self._grid[self._start.row][self._start.column] = Cell.START
        self._grid[self._goal.row][self._goal.column] = Cell.GOAL
    
    def _randomly_fill(self, rows: int, columns: int, sparseness: float):
        # loop through every cell in the maze
        # we are looking at a 10 x 10 maze by default
        for r in range(rows):
            for c in range(columns):
                # if the threshold set by sparseness is exceeded
                # block the cell
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[r][c] = Cell.BLOCKED
    

    def __repr__(self):
        output: str = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + "\n"
        return output



# perform some tests here
# randomly blocking the grid even with a conservative sparseness factor
# such as 20%, can still lead to unsolvable mazes
# a better strategy would be to make use of some form of random walk
# or use a depth-first search to 'create paths' and then block out the paths
# not visited by the dfs
if __name__=='__main__':
    test_maze = Maze()
    print(test_maze)