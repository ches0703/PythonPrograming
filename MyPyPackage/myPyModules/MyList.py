# C:/MyPyPackage/myPyModules/MyList.py
# MyList.py
"""
Project :  User-defined package/module : MyList
Author: Eun-seong Choi
Date of last update: 2022 / 10 / 13
Update list:
    - v1,1 : 10 /13
        Make Module : MyList
        Make funtion : genRandList, shuffleList
                       printListSample
        Add Testing part
"""
import random


def genRandList(L, n):
    for i in range(n):
        L.append(i)
    random.shuffle(L)
    return L


def shuffleList(L):
    random.shuffle(L)
    return L


def printListSample(L, per_line=10, sample_lines=5):
    count = 0
    size = len(L)
    for i in range(0, sample_lines):
        s = ""
        for j in range(0, per_line):
            if count > size:
                break
            s += "{0:>7} ".format(L[count])
            count += 1
        print(s)
        if count >= size:
            break
    if count < size:
        print(' . . . . . .')
        if count < (size - per_line * sample_lines):
            count = size - per_line * sample_lines
    for i in range(0, sample_lines):
        s = ""
        for j in range(0, per_line):
            if count >= size:
                break
            s += "{0:>7} ".format(L[count])
            count += 1
        print(s)
        if count >= size:
            break


if __name__ == "__main__":
    print(__name__)
    L = []
    genRandList(L, 100)
    printListSample(L, 10, 3)
