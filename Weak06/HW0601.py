# HW0601.py
"""
Project :  User-defined package/module selectionSort()
Author: Eun-seong Choi
Date of last update: 2022 / 10 / 13
Update list:
    - v1,1 : 10 /13
        import Modules : C:/MyPyPackage/myPyModules
            MyList, MySortings
        Make Module : MyList, MySortings
"""
import sys
myPyModules_dir = "C:/MyPyPackage/myPyModules"
sys.path.append(myPyModules_dir)
import MyList
import MySortings

L = []
n = 100
MyList.genRandList(L, n)
print("Before Sorting :")
MyList.printListSample(L, 10, 3)
MySortings.selectionSort(L)
print("\nAfter Sorting :")
MyList.printListSample(L, 10, 3)

