from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
from generic_search import dfs, bfs, astar, node_to_path, Node
from timeit import default_timer as timer

class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "■"
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
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(self._columns)] for r in range(self._rows)]
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
    

    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self._goal

    # functions for maze navigation
    # successor returns a list of neighbouring maze locations
    # that can be reached from the current maze location
    def successors(self, ml: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []
        # check the grid location immediately above
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.column))
        # check the grid location immediately below
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1, ml.column))
        # check the grid location immediately to the right
        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column + 1))
        # check the grid location immediately to the left
        if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column - 1))
        return locations

    # function to mark the path from start
    # to the finish of the maze
    def mark(self, path: List[MazeLocation]) -> None:
        for location in path:
            self._grid[location.row][location.column] = Cell.PATH
        self._grid[self._start.row][self._start.column] = Cell.START
        self._grid[self._goal.row][self._goal.column] = Cell.GOAL
    
    def clear(self, path: List[MazeLocation]) -> None:
        for location in path:
            self._grid[location.row][location.column] = Cell.EMPTY
        self._grid[self._start.row][self._start.column] = Cell.START
        self._grid[self._goal.row][self._goal.column] = Cell.GOAL
    
    def __repr__(self): 
        output: str = ""
        for row in self._grid:
            output += " ".join([c.value for c in row]) + "\n"
        return output

# The A* algorithm requires a heuristic 
# The heuristic is used to judge whether the algorithm 
# is getting closer to the goal
# one heuristic usually used is the euclidian distance
def euclidian_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    def distance(ml: MazeLocation) ->float:
        xdist: int = ml.column - goal.column
        ydist: int = ml.row - goal.row
        temp = (xdist * xdist) + (ydist * ydist)
        return sqrt(temp)
    return distance
# the manhattan distance is also used as an heuristic sometimes
def manhattan_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    def distance(ml: MazeLocation):
        xdist: int = abs(ml.column - goal.column)
        ydist: int = abs(ml.row - goal.row)
        return (xdist + ydist)
    return distance
                                                


# perform some tests here
# randomly blocking the grid even with a conservative sparseness factor
# such as 20%, can still lead to unsolvable mazes
# a better strategy would be to make use of some form of random walk
# or use a depth-first search to 'create paths' and then block out the paths
# not visited by the dfs
if __name__=='__main__':
    m = Maze(10, 10)

    # depth-first search
    stime1 = timer()
    solution: Optional[Node[MazeLocation]] = dfs(m._start, m.goal_test, m.successors)
    etime1 = timer()
    if solution is None:
        print("No solution found using depth-first search!")
    else:
        path = node_to_path(solution)
        m.mark(path)
        print(m)
        m.clear(path)
    print(f'time taken: {etime1 - stime1}')
    
    print("\n" + 30*"-" + "\n")
    
    # breadth-first search
    stime2 = timer()
    solution2: Optional[Node[MazeLocation]] = bfs(m._start, m.goal_test,m.successors)
    etime2 = timer()
    if solution2 is None:
        print("No solution found using breadth-first search!")
    else:
        path2: List[MazeLocation] = node_to_path(solution2)
        m.mark(path2)
        print(m)
        m.clear(path2)
    print(f'time taken: {etime2 - stime2}')

    print("\n" + 30*"-" + "\n")

    # a-star algorithm
    distance: Callable[[MazeLocation], float] = euclidian_distance(m._goal)
    stime3 = timer()
    solution3: Optional[Node[MazeLocation]] = astar(m._start, m.goal_test, m.successors, distance)
    etime3 = timer()
    if solution3 is None:
        print('No solution found using astar!')
    else:
        path3 = node_to_path(solution3)
        m.mark(path3)
        print(m)
        m.clear(path3) 
    print(f'time taken: {etime3 - stime3}')