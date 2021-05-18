# There are many ways to caculate pi
# This is one of the more simpler algorithms
# It involves iteratively calculating the series proposed by Leibniz
# This series is as follows: 4/1 - 4/3 + 4/5 - 4/7 + 4/9 ....
# The JIT from Numba was used to speed up some of the calculations

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