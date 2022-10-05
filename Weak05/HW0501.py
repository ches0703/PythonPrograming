# Homework 5.1 (1)
import random
# import time


def genBigRandList(n):
    L = []
    for i in range(n):
        L.append(i)
    random.shuffle(L)
    return L


def printListSample(L, per_line=10, sample_lines=2):

    for i in range(sample_lines):
        for j in range(per_line):
            print("{:10}".format(L[j + (i*10)]), end="")
        print()
    print()
    for i in range(sample_lines):
        for j in range(per_line):
            print("{:10}".format(L[len(L)-(j + (i*10))-1]), end="")
        print()


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


def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        L_left = mergeSort(L[:middle])
        L_right = mergeSort(L[middle:])
    return merge(L_left, L_right)


#Homework 5.1 (2)
#(Application) Performance test of merge sorting


while True:
    print("\nPerformance test of merge sorting algorithm")
    size = int(input("Input size of random list L (0 to quit) = "))
    if size == 0:
        break
    L = genBigRandList(size)

    # testing MergeSorting
    print("\nBefore mergeSort of L :")
    printListSample(L, 10, 2)
    #t1 = time.time()
    sorted_L = mergeSort(L)
    #t2 = time.time()
    print("After mergeSort of L :")
    printListSample(sorted_L, 10, 2)
    #time_elapsed = t2 - t1
    #print("Merge sorting took {} sec".format(time_elapsed))
