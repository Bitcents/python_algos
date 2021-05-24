from __future__ import annotations
from typing import AsyncIterable, Generic, Optional, TypeVar, List, Set, Callable, Deque, Dict, Sequence
from abc import ABC, abstractmethod
from typing_extensions import Protocol
from math import sqrt
from heapq import heappush, heappop


T = TypeVar('T')
V = TypeVar('V')
D = TypeVar('D')
# data structure classes

# refer to node.py
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


# classes related to constraint-satisfactoin problems
# refer to csp.py

class Constraint(Generic[V, D], ABC):
    def __init__(self, variables: List[V]):
        self.variables = variables
    
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]):
        ...

class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables
        self.domains: Dict[V, List[D]] = domains
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constraint[variable] = []
            if variable not in self.domains:
                raise LookupError('Each variable must have an associated domain')
    
    def add_constraint(self, constraint: Constraint[V, D]):
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError('Constraint has variable not in CSP')
            else:
                self.constraints[variable].append(constraint)

    def is_consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        # base case, when there is on assignment for every variable
        if len(self.variables) == len(assignment):
            return assignment
        # create a list of unassigned variables
        # unassigned variables are variables in the CSP which still do not have a value and therefore have not been tested
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.is_consistent(first, local_assignment):
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None


# methods related to searching graphs involving nodes

def dfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
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


def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
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


def astar(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]], heuristic: Callable[[T], float]) -> Optional[Node[T]]:
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


def calculate_pstdev(numbers: Sequence[float], mean: float=None) -> float:
    if mean == None:
        mean: float = sum([num for num in numbers]) / len(numbers)
    else:
        mean = mean
    total: float = 0
    for num in numbers:
       total += (num - mean) ** 2
    return sqrt(total/len(numbers)) 

def zscores(original: Sequence[float]) -> List[float]:
    mean: float = sum([num for num in original]) / len(original)
    pstdev: float = calculate_pstdev(original, mean)
    return [(x - mean)/pstdev for x in original]



