# User‐defined package/module


import sys
myPyModules_dir = "C:/MyPyPackage/myPyModules"
sys.path.append(myPyModules_dir)


import MyList, MySortings
L = []
n = 100
MyList.genRandList(L, n)
print("Before Sorting :")
MyList.printListSample(L, 10, 3)
MySortings.selectionSort(L)
print("\nAfter Sorting :")
MyList.printListSample(L, 10, 3)

