# Exam1B - Application of class Mtrx for float data type
# 21912070 최은성

# Main Part
from Class_Mtrx import *

if __name__ == "__main__":
    print("2022-2 컴사파Exam1B_21912070_최은성")
    La = [0.0, 1.1, 2.2, 3.3,\
    4.4, 5.5, 6.6, 7.7,\
    8.8, 9.9, 1.5, 2.5]
    Lb = [1.0, 0.0, 0.0, 0.0,\
    0.0, 1.0, 0.0, 0.0,\
    0.0, 0.0, 1.0, 0.0]
    Lc = [1.0, 0.0, 0.0,\
    0.0, 1.0, 0.0,\
    0.0, 0.0, 1.0,\
    0.0, 0.0, 0.0,\
    0.0, 0.0, 0.0]
    mA = Mtrx("mA", 3, 4, La); print(mA)
    mB = Mtrx("mB", 3, 4, Lb); print(mB)
    mC = Mtrx("mC", 4, 3, Lc); print(mC)
    mD = mA + mB; mD.set_name("mD = mA + mB"); print(mD)
    mE = mA - mB; mE.set_name("mE = mA - mB"); print(mE)
    mF = mA * mC; mF.set_name("mF = mA * mC"); print(mF)
    mG = mA.transpose(); mG.set_name("mG = mA.transpose()"); print(mG)