# numpy의 import
import numpy as np

# 선형시스템 AX = B에서 A와 B의 준비

# - numpy 배열 A의 생성 및 출력
A = np.array([
    [1, 5, 3, 3, 7],
    [3, 4, 5, 6, 7],
    [1, 3, 5, 7, 9],
    [3, 1, 4, 1, 5],
    [5, 5, 3, 3, 1],
])
print("A = \n", A)

# - numpy 배열 B의 생성 및 출력
B = np.array([105, 135, 145, 74, 75])
print("B = \n", B)

# - 배열 A의 행렬식 (det_A) 계산 및 출력
Det_A = np.linalg.det(A)
print("Det_A = \n", Det_A)

# - 배열 A의 역행렬 (inv_A) 계산 및 출력
Inv_A = np.linalg.inv(A)
print("Inv_A = \n", Inv_A)

# - 선형시스템 AX = B의 해 (solution)인 X의 산출 및 출력
X = np.linalg.solve(A, B)
print("X = \n", X)

# - B1 = A * X의 계산 및 B1 출력
B1 = np.matmul(A, X)
print("B1 = A * X = \n", B1)

X1 = np.matmul(Inv_A, B)
print("X1 = Inv_A * B = \n", X1)
