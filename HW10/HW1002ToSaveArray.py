# HW1002ToSaveArray.py
"""
Project : Calculate the Matrix with numpy module
Author: Eun-seong Choi
Date of last update: 2022 / 11 / 17
Update list:
    - v1.1 : 11 / 17
        Write 7 x 7 matrix, save to HW10/7x7Array.txt
"""
import numpy as np
A = [
    [1, 2, 3, 4, 5, 6, 7],
    [9, 8, 7, 6, 5, 4, 3],
    [3, 7, 5, 1, 0, 1, 2],
    [4, 1, 0, 2, 8, 3, 7],
    [9, 7, 3, 2, 1, 6, 5],
    [7, 5, 3, 1, 2, 4, 6],
    [1, 3, 5, 7, 9, 8, 7]
]

np.savetxt("HW10/7x7Array.txt", A)
