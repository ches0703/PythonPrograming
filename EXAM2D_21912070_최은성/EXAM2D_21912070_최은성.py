# MySortings.py
"""
Project :  EXAM2D
Author: Eun-seong Choi
Date of last update: 2022 / 12 / 11
Update list:
    - v1,1 : 12 /11
        import user defined module : MyList, MySortings
        import : time, numpy, random
"""
import MyList
import MySortings
import time
import numpy
import random

def main():
    print("2022-2 컴사파 기말고사 학번: 211912070, 이름: 최은성")
    Test_size = [100000, 500000, 1000000, 5000000]
    for L_size in Test_size:
        print("\nGenerating random list of size ({}) ...".format(L_size))
        L = MyList.genRandFloatList(L_size)

        # testing Numpy.sort()
        print("Before numpy.sort() of L :")
        MyList.printFloatListSample(L, 10, 2)
        t1 = time.time()
        L = numpy.sort(L)
        t2 = time.time()
        print("After numpy.sort() of L :")
        MyList.printFloatListSample(L, 10, 2)
        time_elapsed = t2 - t1
        print("numpy.sort() of list (size={}) took {} sec".format(
            L_size, time_elapsed))
        # testing Quick Sorting
        random.shuffle(L)
        print("\nBefore MySortings.quickSort() of L :")
        MyList.printFloatListSample(L, 10, 2)
        t1 = time.time()
        MySortings.quickSort(L)
        t2 = time.time()
        print("After MySortings.quickSort() of L :")
        MyList.printFloatListSample(L, 10, 2)
        time_elapsed = t2 - t1
        print("MySortings.quickSort() of list (size={}) took {} sec"
              .format(L_size, time_elapsed))


if __name__ == "__main__":
    main()
