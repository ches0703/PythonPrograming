# fibo
import time


def srFibo(n):
    if n <= 1:
        return n
    else:
        return srFibo(n - 1) + srFibo(n - 2)


memo = dict()


def dynFibo(n):
    if n in memo:
        return memo[n]
    elif n <= 1:
        memo[n] = n
        return n
    else:
        memo[n] = dynFibo(n - 1) + dynFibo(n - 2)
        return memo[n]


if __name__ == "__main__":
    t1 = time.time()
    srFibo(30)
    t2 = time.time()
    print("srFibo time = ", t2 - t1)

    t1 = time.time()
    dynFibo(30)
    t2 = time.time()
    print("dynFibo time = ", t2 - t1)

