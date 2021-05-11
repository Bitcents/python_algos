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