import numpy as np

A = np.arange(10)
print("A = ", A)
print("A[0] = ", A[0])
print("A[0] = ", A[-1])
print("A[0] = ", A[:5])
print("A[0] = ", A[::2])
A[:5] = 10
print("A[0] = ", A)
B = A[5:]
print("B = A[5:]", B)

B[0] = 20
print("(B[0] = 20)A = ", A)

C = A[5:].copy()
print(C)
C[0] = 30
print("((copy A[5:])C[0] = 30)A = ", A)
