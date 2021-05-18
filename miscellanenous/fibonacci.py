from timeit import default_timer as time
from typing import Generator

# find the nth fibonacci number
def fib(n:int):
    prev = 0
    next = 1
    for _ in range(1, n):
        temp = next
        next = next + prev
        prev = temp
    return next

# generator function to yield every fibonacci number
# until the nth fibonacci number
def fib_gen(n:int) -> Generator[int, None, None]:
    yield 0 # special case
    if n > 0:
        last: int = 0
        next: int = 1
        for _ in range(1, n):
            last, next = next, next + last
            yield next


if __name__=='__main__':
    s_time = time()
    fib_nums = fib_gen(15)
    e_time = time()
    print(f"total time taken: {e_time - s_time}")
    for number in fib_nums:
        print(f"{number}")