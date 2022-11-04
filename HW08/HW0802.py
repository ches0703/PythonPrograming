# HW0802.py
"""
Project : Homework 8.2 - Application Program of myClassMtrx
Author: Eun-seong Choi
Date of last update: 2022 / 11 / 04
Update list:
    - v1.1 : 10 / 18
        Import Class_Mtrx
        Make Funthion : 
            fgetMtrx
        Add Application
"""
from Class_Mtrx import Mtrx


# get Matrix data to file
def fgetMtrx(name, f_in):
    # Get mtrix data : row col
    row, col = map(int, fin.readline().split())
    # Read Data and save to list
    Mtrx_array = []
    for i in range(row):  # Redline() * n(row)
        Mtrx_array.extend(list(map(float, fin.readline().split())))
    # Make Matrix with mtrix data array
    return Mtrx(name, row, col, Mtrx_array)


# Application
if __name__ == "__main__":
    # File Relative Path
    fin = open("matrix_data.txt", "r")
    fout = open("result.txt", "w")

    mA = fgetMtrx("mA", fin)
    print(mA)
    fout.write("{}".format(mA))

    mB = fgetMtrx("mB", fin)
    print(mB)
    fout.write("{}".format(mB))

    mC = fgetMtrx("mC", fin)
    print(mC)
    fout.write("{}".format(mC))
    fin.close()

    mD = mA + mB
    mD.setName("mD = mA + mB")
    print(mD)
    fout.write("{}".format(mD))

    mE = mA - mB
    mE.setName("mE = mA - mB")
    print(mE)
    fout.write("{}".format(mE))

    mF = mA * mC
    mF.setName("mF = mA * mB")
    print(mF)
    fout.write("{}".format(mF))

    fout.close()
