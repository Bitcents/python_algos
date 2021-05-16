from typing import Generic, TypeVar, List, Deque, Set
from heapq import heappop, heappush
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

