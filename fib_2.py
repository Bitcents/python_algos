from timeit import default_timer as time
from typing import Dict
from functools import lru_cache

@lru_cache(maxsize=None)
def fib2(n:int) -> int:
    if n < 2:
        return n
    return fib2(n-2) + fib2(n-1)

if __name__=='__main__':
    start_time = time()
    number = fib2(15)
    end_time = time()

    print(f"The fibonacci number is: {number}. The time taken was {end_time - start_time}")