"""
Project :  User-defined package/module MyMatrix
Author: Eun-seong Choi
Date of last update: 2022 / 10 / 13
Update list:
    - v1,1 : 10 /13
        import Modules : C:/MyPyPackage/myPyModules
              MyMatrix
        Make Moduls : MyMatrix
"""
import sys
sys.path.append("C:/MyPyPackage/myPyModules")
import MyMatrix

A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 1]]
B = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1]]
C = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]

MyMatrix.printMtrx("A", A)
MyMatrix.printMtrx("B", B)
MyMatrix.printMtrx("C", C)
D = MyMatrix.addMtrx(A, B)
MyMatrix.printMtrx("A + B", D)
E = MyMatrix.subMtrx(A, B)
MyMatrix.printMtrx("A - B", E)
F = MyMatrix.mulMtrx(A, C)
MyMatrix.printMtrx("A * C", F)
