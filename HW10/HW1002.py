import numpy as np

# Get Array Data for loadtxt()
A = np.loadtxt("HW10/7x7Array.txt")
print(A)

# Calc Determinant
A_det = np.linalg.det(A)
print("A_det = ", A_det)

# Calc A's inverse
A_inv = np.linalg.inv(A)
print("A_inv = \n", A_inv)

# Use matmul for Print A * A_inv
E = np.matmul(A, A_inv)
print("E = np.matmul(A, A_inv) = \n", A_inv)
