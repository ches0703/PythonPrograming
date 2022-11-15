import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
print("A = ", A)
print("A.type = ", A.dtype)
print("A.dim = ", A.ndim)
print("A.shape = ", A.shape)
print("A.size = ", A.size)
print("A.itemsize", A.itemsize)
print("A.data = ", A.data)

print()

B1 = np.arange(3)
print("B1 = ", B1)
print("B1.type = ", B1.dtype)

B2 = np.arange(3)
print("B2 = ", B2)
print("B2.type = ", B2.dtype)

B3 = np.arange(3, 10)
print("B3 = ", B3)
print("B3.type = ", B3.dtype)

B4 = np.arange(3, 10, 2)
print("B4 = ", B4)
print("B4.type = ", B4.dtype)

print()

C1 = np.zeros((2, 3))
print("C1 = ", C1)

C2 = np.ones((2, 3))
print("C2 = ", C2)

C3 = np.empty((2, 3))
print("C3 = ", C3)

C4 = np.full((2, 3), 10, dtype=None, order='C')
print("C4 = ", C4)

print()

D1 = np.identity(3)
print("D1 = \n", D1)

D2 = np.eye(3, dtype=int)
print("D2 = \n", D2)

D3 = np.eye(3, k=1, dtype=int)
print("D1 = \n", D3)

D4 = np.eye(3, k=-1, dtype=int)
print("D4 = \n", D4)
