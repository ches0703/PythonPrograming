# C:/MyPyPackage/myPyModules/MyMatrix.py\
# MyMatrix.py
"""
Project :  User-defined package/module : MyMatrix
Author: Eun-seong Choi
Date of last update: 2022 / 10 / 13
Update list:
    - v1,1 : 10 /13
        Make Module : MyMatrix
        Make funtion : printMtrx, addMtrx
                       subMtrx, mulMtrx
"""


# Print Matrix
def printMtrx(name, M):
    print(name + " = ")
    for i in M:
        for j in i:
            print("{:3}".format(j), end="")
        print()


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