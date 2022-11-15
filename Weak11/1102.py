import numpy as np

A = np.arange(10)
print("A = \n", A)
print("A dim = ", A.ndim)
print("A.Shape = ", A.shape)

B = A.reshape((2, 5))
print("B = \n", B)
print("B dim = ", B.ndim)
print("B.Shape = ", B.shape)

C = A.reshape((5, -1))
print("C = \n", C)
print("C dim = ", C.ndim)
print("C.Shape = ", C.shape)

A.shape = (5, 2)
print("A.Shape(5, 2) = \n", A)

D = B.ravel()
print("D = ", D)
E = B.flatten()
print("E = ", E)

F = np.arange(15).reshape(5, 3)
print("F = \n", F)
FT = F.T
print("FT = \n", FT)