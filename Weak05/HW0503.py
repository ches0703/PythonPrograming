# HW0503.py
"""
Project : Dynamic Programming for Fibonacci Series
Author: Eun-seong Choi
Date of last update: 2022 / 10 / 06
Update list:
    - v1,1 : 10 /6
        Make a recursive part
        Add memo & memo's algorithm
"""

# Import part
import time
memo = dict()


# recursive calculation with memoization
def dynFibo(n):
    if n < 0:  # Termination condition
        return None
    elif 0 <= n < 2:  # n = 0, or 1
        return n
    else:
        if n in memo:
            # memo's algorithm : return saved value
            return memo[n]
        else:
            # memo's algorithm : save value & recursive part
            memo[n] = result = dynFibo(n-1) + dynFibo(n-2)
            return result


# (Application)
(start, stop, step) = tuple(
    map(int,
        input("input start, stop, step of Fibonacci series : ").split(' ')))
for n in range(start, stop+1, step):
    t_before = time.time()
    fibo_n = dynFibo(n)
    t_after = time.time()
    t_elapse_us = t_after - t_before
    print("dynFibo({:3d}) = {:25d}, took {:10.2f}[micro_sec]".format(
        n, fibo_n, t_elapse_us))
