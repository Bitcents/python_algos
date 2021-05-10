import typing
from numba import jit

@jit(nopython=True)
def calculate_pi(n: int) -> float:
    pi:float = 0.0
    numerator: float = 4.0
    denominator: float = 1.0
    factor: float = 1.0
    for _ in range(n):
        pi += factor*(1.0/denominator)
        denominator += 2.0
        factor *= -1.0
    return pi*numerator


if __name__=='__main__':
    pi = calculate_pi(300000000)
    print(pi)