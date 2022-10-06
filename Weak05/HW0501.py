# HW0501.py
"""
Project : Performance test of merge sorting
Author: Eun-seong Choi
Date of last update: 2022 / 10 / 06
Update list:
    - v1,1 : 10 /6
        Make a funtion of genBigRandList(n)
        Make a funtion of printListSample(L, per_line=10, sample_lines=2)
        Make a funtion of merge(L_left, L_right), mergeSort(L)
        add performance testing
"""

# Impoer part
import random
import time


# Homework 5.1 (1) - Make rand list(Not Duplicate)
def genBigRandList(n):
    L = []
    for i in range(n):
        L.append(i)
    random.shuffle(L)
    return L


# Homework 5.1 (2) - Print List sample funtion
def printListSample(L, per_line=10, sample_lines=2):
    for i in range(sample_lines):
        for j in range(per_line):
            print("{:10}".format(L[j + (i*10)]), end="")
        print()
    print("Skip . . .")
    for i in range(sample_lines):
        for j in range(per_line):
            print("{:10}".format(
                L[(len(L)-(per_line * sample_lines))+(j + (i * 10))]),
                end="")
        print()


# Homework 5.1 (3) - Merge sort - sort part
def merge(L_left, L_right):
    L_res = []
    i, j = 0, 0
    len_left, len_right = len(L_left), len(L_right)
    while i < len_left and j < len_right:
        if L_left[i] < L_right[j]:
            L_res.append(L_left[i])
            i += 1
        else:
            L_res.append(L_right[j])
            j += 1
    while (i < len_left):
        L_res.append(L_left[i])
        i += 1
    while (j < len_right):
        L_res.append(L_right[j])
        j += 1
    return L_res


# Merge sort - divide part, recursion part
def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        L_left = mergeSort(L[:middle])
        L_right = mergeSort(L[middle:])
    return merge(L_left, L_right)


# Homework 5.1 (2) - (Application) Performance test of merge sorting
while True:

    # Make list
    print("\nPerformance test of merge sorting algorithm")
    size = int(input("Input size of random list L (0 to quit) = "))
    if size == 0:
        break
    L = genBigRandList(size)

    # testing MergeSorting
    print("\nBefore mergeSort of L :")
    printListSample(L, 10, 2)
    t1 = time.time()    # Save start time
    sorted_L = mergeSort(L)
    t2 = time.time()    # Save end time
    print("After mergeSort of L :")
    printListSample(sorted_L, 10, 2)
    time_elapsed = t2 - t1  # Calc duraition
    print("Merge sorting took {} sec".format(time_elapsed))
