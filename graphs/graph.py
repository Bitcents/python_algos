from typing import TypeVar, Generic, List, Optional
from graphs.edge import Edge

V = TypeVar('V')

class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self.edges: List[List[Edge]] = [[] for _ in vertices]