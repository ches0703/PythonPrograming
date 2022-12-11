# MyList.py
"""
Project :  EXAM2D MyList
Author: Eun-seong Choi
Date of last update: 2022 / 12 / 11
Update list:
    - v1,1 : 10 /13
        Make funtion : genRandFloatList
                       printFloatListSample

"""
import random


# Return float ramdom list
def genRandFloatList(L_size):
    L = []
    for i in range(L_size):
        # Add in List : -1 * L_size / 200 < value < L_size / 200
        value = random.uniform(-1 * L_size / 200, L_size / 200)
        # for fast testing -> commit
        ''' # For Not duplicate
        if value in L:  
            continue
        else:
            L.append(value)
        '''
        L.append(value)
    return L


# Print List's Sample
def printFloatListSample(L, per_line=10, sample_lines=5):
    count = 0
    size = len(L)
    # line 0 ~ line sample_lines
    for i in range(0, sample_lines):
        s = ""
        for j in range(0, per_line):
            if count > size:
                break
            s += "{0:>7.2} ".format(L[count])  # decimal point : under 2
            count += 1
        print(s)
        if count >= size:
            break
    if count < size:
        print(' . . . . . .')
        if count < (size - per_line * sample_lines):
            count = size - per_line * sample_lines

    # before sampleline line from lastline ~ last line
    for i in range(0, sample_lines):
        s = ""
        for j in range(0, per_line):
            if count >= size:
                break
            s += "{0:>7.2} ".format(L[count])  # decimal point : under 2
            count += 1
        print(s)
        if count >= size:
            break


