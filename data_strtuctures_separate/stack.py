from typing import TypeVar, Generic, List

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

