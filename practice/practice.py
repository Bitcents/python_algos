from typing import Generic, Optional, TypeVar, List, Set, Callable, Deque, Dict
from typing_extensions import Protocol
from heapq import heappush, heappop
from __future__ import annotations
T = TypeVar('T')

# check generic_search.py
class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node[T]], cost: float, heuristic: float) -> None:
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
    
    def __lt__(self, other: Node[T]) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

# check stack.py
class Stack(Generic[T]):
    def __init__(self) -> None:
        # we will use Python lists to implement a stack
        self._container: List[T] = []
    
    @property
    def is_empty(self) -> bool:
        return self._container == None 

    def pop(self) -> T:
        self._container.pop()
    
    def push(self, item: T) -> None:
        self._container.append(item)
    
    def __repr__(self) -> str:
        return repr(self._container)

# check queue.py
class Queue(Generic[T]):
    def __init__(self) -> None:
        self._container: Deque[T] = Deque()
    
    @property
    def is_empty(self) -> bool:
        return self._container == None

    def pop(self) -> T:
        self._container.popleft()
    
    def push(self, item: T) -> None:
        self._container.append(item)
    
    def __repr__(self) -> str:
        return repr(self._container)


# check priority_queue.py
class PriorityQueue(Generic[T]):
    def __init__(self):
        self._container: List[T] = []

    @property
    def is_empty(self):
        return self._container == None

    def pop(self) -> T:
        return heappop(self._container)
    
    def push(self, item: T) -> None:
        heappush(self._container, item)
    
    def __repr__(self) -> str:
        return repr(self._container)


class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node], cost: float=0.0, heuristic: float=0.0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        
    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def dfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional(Node[T]):
    # initlalize stack and populate with initial node
    frontier: Stack[Node[T]] = Stack()
    frontier.push(Node(initial, None))
    # initialze set of explored nodes
    explored: Set[T] = Set()
    explored.add(T)
    # loop until frontier is not empty:
    while not frontier.is_empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            else:
                frontier.push(child)
                explored.add(child)


def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional(Node[T]):
    # intialize queue and populate with initial node
    frontier: Queue[Node[T]] = Queue()
    frontier.push(Node[T], None)
    # initialze set of explored nodes
    explored: Set[T] = Set()
    explored.add(T)
    # loop while frontier is not empty
    while not frontier.is_empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            else:
                frontier.push(child)
                explored.add(child)


def astar(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]], heuristic: Callable[[T], float]) -> Optional(Node[T]):
    frontier: PriorityQueue[Node[T]] = PriorityQueue()
    frontier.push(Node[initial, None, 0.0, heuristic(initial)])
    explored: Dict[T, float] = {initial : 0.0}
    while not frontier.is_empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            new_cost = current_node.cost + 1
            if not child in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child))) 
