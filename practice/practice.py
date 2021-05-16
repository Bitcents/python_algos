# This is the file where I try to rewrite all the other code in this project
# This should eventually become the biggest file
# I will put references where necessary


from typing import Generic, Optional, TypeVar, List, Set, Callable, Deque
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

