import numpy as np

A = np.arange(10).reshape((2, 5))
print("A = \n", A)
B = A + 10
print("B = \n", B)

C = A * 10 - 50
print("C = \n", C)
C = abs(C)
print("C = (abs(C)) = \n", C)

D = A < 5
print("D = A < 5 \n", D)
print("D.any() = ", D.any())
print("D.all() = ", D.all())

E = np.logical_and(A % 2 == 0, A > 5)
print("E = \n", E)

F = np.logical_or(A % 2 == 0, A > 5)
print("E = \n", F)

ND = np.logical_not(D)
print("ND = \n", ND)