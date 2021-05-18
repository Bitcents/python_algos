from typing import Generic, TypeVar, Optional
from __future__ import annotations
T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node], cost: float=0.0, heuristic: float=0.0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        
    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)