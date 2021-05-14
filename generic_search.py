from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from typing_extensions import Protocol
from heapq import heappush, heappop 
from timeit import default_timer as timer

T = TypeVar('T')


C = TypeVar("C", bound="Comparable")

class Comparable(Protocol):
    def __eq__(self: C, other: Any) -> bool:
        ...
    def __lt__(self: C, other: C) -> bool:
        ...
    def __gt__(self: C, other: C) -> bool:
        return self < other and self != other
    def __le__(self: C, other: C) -> bool:
        return self < other or self == other
    def __ge__(self: C, other: C) -> bool:
        return not self < other



# The stack data structure was defined elsewhere
# but let us re-implement it here, just for fun :D

class Stack(Generic[T]):
    def __init__(self) -> None:
        # we use lists to implement the stack
        self._container: List[T] = []
    
    @property
    def empty(self) -> bool:
        return not self._container

    def pop(self) -> T:
        if len(self._container) > 0:
            return self._container.pop()
        else:
            # do nothing if stack is empty
            return

    def push(self, item: T) -> None:
        self._container.append(item)
    
    def __repr__(self) -> str:
        # prints the stack from top to bottom
        # a stack usually does not have a print function
        # I include one for debugging purposes
        output_str = None
        if len(self._container) > 0:
            output_str = "\n".join([str(self._container[i]) for i in range(len(self._container) - 1, 0, -1)])
        else:
            output_str = "stack is empty"
        return output_str

# breadt-frst search employs the same algorithm as depth-first search
# the only difference being the data structure used in each case
# while dfs uses a stack bfs uses a queue 
class Queue(Generic[T]):
    def __init__(self) -> None:
        self._container: Deque[T] = Deque()
    
    @property
    def is_empty(self) -> bool:
        return not self._container
    
    def push(self, item: T) -> None:
        self._container.append(item)
    
    def pop(self) -> T:
        return self._container.popleft()

    def __repr__(self) -> str:
        return repr(self._container)

# Dfs and bfs is usually performed on a collection of nodes
# We will define the node class here
class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node], cost: float=0.0, heuristic: float=0.0) -> None:
        self.state: T = state
        self.cost: float = cost
        self.heuristic: float = heuristic
        self.parent: Optional[Node] = parent

    def __lt__(self, other: Node) -> bool:
        return(self.cost + self.heuristic < (other.cost + other.heuristic))
    

# The priority queue abstract data structure is essential 
# to the functioning of the A* algorithm 
# we implement a priority queue using the heappop and heappush methods
# from the heapq module
# the structure has a similar structure to the Queue and Stack classes
class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    
    @property
    def is_empty(self) -> bool:
        return not self._container
    
    def push(self, item: T) -> None:
        heappush(self._container, item)
    
    def pop(self) -> T:
        return heappop(self._container)

    def __repr__(self) -> None:
        return repr(self._container)


# Binary search depends on the sequence being sorted
# It will not work on unsorted lists, for example
def binary_contains(sequence: Sequence[C], key: C) -> bool:
    low: int = 0
    high: int = len(sequence) - 1

    while low <= high:
        mid: int = (low + high) // 2
        if sequence[mid] < key:
            high = mid - 1
        elif sequence[mid] > key:
            left = mid + 1
        else:
            return True
    return False

# The simplest way to search for something
# This will work whether the sequence in question is sorted or not
def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    
    return False




def dfs(initial: T, goal_test: Callable[[T], bool], successors:+ Callable[[T], List[T]]) -> Optional[Node[T]]:
    # We store discovred but unexplored nodes to the unexplored stack
    frontier: Stack[Node[T]] = Stack()
    # The initial node will always be the starting point of the dfs
    # We therefore push the initial node into the stack
    frontier.push(Node(initial, None))
    # We alse need to store explored nodes so we do not move around in loops
    explored: Set[T] = {initial}
    # Keep going while there are still nodes inside unexplored:
    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node
        # check for paths from current node
        for child in successors(current_state):
            # if the child is in explored, ignore and continue
            if child in explored:
                continue
            else:
                explored.add(child)
                frontier.push(Node(child, current_node))


def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional(Node[T]):
    # make a frontier queue
    frontier: Queue[Node[T]] = Queue()
    # and push the initial node into it
    frontier.push(Node(initial, None))
    # create a set of explored T
    explored: Set[T] = {initial}
    # continue searching until there are nodes in the frontier
    # or the goal is found 
    while not frontier.is_empty:
        current_node: Node[T] = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            else:
                explored.add(child)
                frontier.push(Node(child, current_node))

# one of the better search algorithms out there
# the a star algorithm augments the typical breadth-first search
def astar(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]], heuristic: Callable[[T], float]) -> Optional(Node[T]):
    frontier: PriorityQueue[Node[T]] = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    explored: Dict[T, float] = {initial : 0.0}

    while not frontier.is_empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            new_cost: float = current_node.cost + 1
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child) ))
    


# We want to know the path that needs to be taken
# from the starting node to reach the goal node
def node_to_path(node: Node[T]) -> List:
    # create a list of nodes
    # the node passed into the function muset be on the path
    # hence the list has the node as one of its elements
    path: List[T] = [node.state]
    # loop until the node has no parent
    # since the startint node has no parent
    # the loop will stop there
    while node.parent != None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path

# perform some tests and make some comparisons

if __name__ == "__main__":
    list = [1, 5, 15, 15, 15, 15, 20, 21, 22, 25, 30, 31, 32, 50, 51, 100, 121, 122, 123, 124, 137]
    
    s_time_1 = timer()
    linear_test = linear_contains(list, 30)
    e_time_1 = timer()
    
    s_time_2 = timer()
    binary_test = binary_contains(list, 30)
    e_time_2 = timer()


    print(f'linear test result: {linear_test}. Time taken: {e_time_1 - s_time_1}')
    print(f'binary test result: {binary_test}. Time taken: {e_time_2 - s_time_2}')

    # print(binary_contains(["a", "d", "e", "f", "z"], "f")) # True
    # print(binary_contains(["john", "mark", "ronald", "sarah"], "sheila")) #False  

    # It should be clear from the results that for short sequences
    # Linear searching would be faster than binary searching
    # However, once the data set grows large enough,
    # Binary searching would be much faster

        # stack tests
    test_list = [1,2,3,4,5,6,7,8,9]
    test_stack = Stack()
    for item in test_list:
        test_stack.push(item)
    top_item = test_stack.pop()
    print(test_stack)
