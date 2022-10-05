PI = 3.141592


def findMinMax(L):
    min = max = L[0]
    for i in L:
        if min > i:
            min = i
        if max < i:
            max = i
    return min, max


def circleCalc(radius):
    return 2*PI*radius, PI*radius*radius


L = [2, 8, 9, 6, 4, 2, 23, 0, 4, 10]
L_min, L_max = findMinMax(L)
print("L :", L)
print("Min : {}, Max = {}".format(L_min, L_max))

circum, area = circleCalc(10)
print("radius = {}, circun = {}, area = {}"
      .format(10, circum, area))
