# HW1002.py
"""
Project : Calculate the Matrix with numpy module
Author: Eun-seong Choi
Date of last update: 2022 / 11 / 17
Update list:
    - v1.1 : 11 / 17
        Make py file for textfile save : HW1002ToSaveArray,py
        Load file : HW10/7x7Array.txt 
        Save to A array as Loaded file
        Calc : A_det, A_inv, A * A_inv

"""
import numpy as np

# Get Array Data for loadtxt()
A = np.loadtxt("HW10/7x7Array.txt")
print("A = \n", A)

# Calc Determinant
A_det = np.linalg.det(A)
print("A_det = ", A_det)

# Calc A's inverse
A_inv = np.linalg.inv(A)
print("A_inv = \n", A_inv)

# Use matmul for Print A * A_inv
E = np.matmul(A, A_inv)
print("E = np.matmul(A, A_inv) = \n", E)
