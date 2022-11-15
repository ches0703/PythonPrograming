import numpy as np

A = np.arange(12).reshape((4, 3))
print("A = \n", A)
print("A.smm() = ", A.sum())
print("A.smm(0) = ", A.sum(0))
print("A.smm(1) = ", A.sum(1))
print("A.smm(-1) = ", A.sum(-1))

B = np.arange(27).reshape((3, 3, 3))
print("B = \n", B)
print("B.shape() =  ", B.shape)

print("B.sum() = ", B.sum())
print("B.sum(0) = \n", B.sum(0))
print("B.sum(1) = \n", B.sum(1))
print("B.sum(2) = \n", B.sum(2))
print("B.sum(-1) = \n", B.sum(-1))