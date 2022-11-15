import numpy as np

A = np.arange(12).reshape((3, 4))
print("A = \n", A)
print("A.shpae = ", A.shape)
print("A[0] = ", A[0])
print("A[:2] = \n", A[:2])

B = A[:, 1:3]
print("B = A[:, 1:3]\n", B)

C = A[:, :1]
print("C = A[:, :1]\n", C)

D = A[:, 1:3].copy() 
A[:, 1:3] = -1
print("D = \n", D)

print("A = \n", A)
