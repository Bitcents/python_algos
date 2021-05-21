from typing import Generic, TypeVar, List, Deque, Set, Tuple, Iterable, Iterator
from heapq import heappop, heappush
from math import sqrt
from __future__ import annotations


T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    
    def push(self, item: T):
        self._container.append(item)
    
    def pop(self) -> T:
        return self._container.pop()
    # a traditional stack should not have to implement a print function
    # however I include one for better examination of the stack's content
    # this helps in testing and debugging
    def __repr__(self) -> str:
        return repr(self._container)


class Queue(Generic[T]):
    def __init__(self) -> None:
        self._container: Deque[T] = Deque()
    
    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self)  -> T:
        return self._container.popleft()
    
    def __repr__(self) -> str:
        return repr(self._container)
        

class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    
    def push(self, item: T) -> None:
        heappush(self._container, item)
    
    def pop(self) -> T:
        return heappop(self._container)

    def __repr__(self):
        return repr(self._container)


class DataPoint:
    def __init__(self, initial: Iterable[float]) -> None:
        self._originals: Tuple[float, ...] = tuple(initial)
        self.dimensions: Tuple[float, ...] = tuple(initial)

    @property
    def num_dimensions(self):   
        return len(self.dimensions)
    
    def distance(self, other: DataPoint) -> float:
        if self.num_dimensions != other.num_dimensions:
            raise ValueError('points do not have the same dimensions')
        else:
            combined: Iterator[Tuple[float, float]] = zip(self, other)
            differences:  List[float] = [(x - y) ** 2 for x,y in combined]
            return sqrt(sum(differences))
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(self, other):
            return NotImplemented
        else:
            return self.dimensions == other.dimensions

    def __repr__(self) -> str:
        return self.dimensions.__repr__()
