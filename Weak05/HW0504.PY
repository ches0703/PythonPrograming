# HW0504.py
"""
Project : Matrix clac
Author: Eun-seong Choi
Date of last update: 2022 / 10 / 06
Update list:
    - v1,1 : 10 /6
        Make a funtion of printMtrx(name, M)
        Make a funtion of Matrix Calc
            - Add, Sub, Mul
"""


# Homework 5.4 (1) - Print Matrix
def printMtrx(name, M):
    print(name + " = ")
    for i in M:
        for j in i:
            print("{:3}".format(j), end="")
        print()


# Homework 5.4 (2) - Calc Matrix

# Add funtion
def addMtrx(M1, M2):
    # Make list & initialization : row = M1.row, col = M1.col
    R = [[0 for i in range(len(M1[j]))] for j in range(len(M1))]
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            R[i][j] = M1[i][j] + M2[i][j]
    return R


# Sub funtion
def subMtrx(M1, M2):
    # Make list & initialization : row = M1.row, col = M1.col
    R = [[0 for i in range(len(M1[j]))] for j in range(len(M1))]
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            R[i][j] = M1[i][j] - M2[i][j]
    return R


# Mul funtion
def mulMtrx(M1, M2):
    # Make list & initialization : row = M1.row, col = M2.col
    R = [[0 for i in range(len(M2[j]))] for j in range(len(M1))]
    for i in range(len(R)):
        for j in range(len(R[i])):
            for k in range(len(M1[i])):
                R[i][j] += M1[i][k] * M2[k][j]
    return R


# main funtion
def main():
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 1]]
    B = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1]]
    C = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
    printMtrx("A", A)
    printMtrx("B", B)
    printMtrx("C", C)
    D = addMtrx(A, B)
    printMtrx("A + B", D)
    E = subMtrx(A, B)
    printMtrx("A - B", E)
    F = mulMtrx(A, C)
    printMtrx("A * C", F)


if __name__ == "__main__":
    main()
