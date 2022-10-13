# C:/MyPyPackage/myPyModules/MySortings.py
# MySortings.py
"""
Project :  User-defined package/module : MySortings
Author: Eun-seong Choi
Date of last update: 2022 / 10 / 13
Update list:
    - v1,1 : 10 /13
        Make Module : MySortings
        Make funtion : selectionSort
    - v1,2 : 10 /13
        Make funtion : _merge, _mergeSort, mergeSort
"""


# SelectionSort
def selectionSort(L):
    for i in range(len(L)):
        min_index = i
        for j in range(i, len(L)):
            if L[j] < L[i]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]


# MergeSort
def _merge(L_left, L_right):
    L_result = []
    i, j = 0, 0
    while i < len(L_left) and j < len(L_right):
        if L_left[i] < L_right[j]:
            L_result.append(L_left[i])
            i += 1
        else:
            L_result.append(L_right[j])
            j += 1
    while (i < len(L_left)):
        L_result.append(L_left[i])
        i += 1
    while (j < len(L_right)):
        L_result.append(L_right[j])
        j += 1
    return L_result


def _mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        L_left = _mergeSort(L[:middle])
        L_right = _mergeSort(L[middle:])
        L_result = _merge(L_left, L_right)
        return L_result


def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        L_result = _mergeSort(L)
    for i in range(len(L)):
        L[i] = L_result[i]