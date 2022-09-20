# Data Type


# List
L1 = [1, 2, 3, 4, 5]
print("L1 : ", L1)
print("len(L1) : ", len(L1))
L1_sum = 0
for i in range(len(L1)):
    L1_sum += L1[i]
print("L1 Sum : ", L1_sum)

L2 = list()
for i in range(0, 10, 2):
    L2.append(i)
print("L2 : ", L2)

# Bool
x = True
y = False

print("x = {}, y = {}".format(x, y))
print("x or y : ", x or y)
print("x or x : ", x or x)
print("y or y : ", y or y)
print("x and y : ", x and y)
print("x and x : ", x and x)
print("y and y : ", y and y)
print("not x : ", not x)

# Calc
print("4 ** 3 = ", 4**3)
print("3.8 // 1.2 = ", 3.8//1.2)

# List funtion

L3 = []
print("Input 10 integer data")
while len(L3) < 10:
    L3.append(int(input("Data : ")))
print(L3)
print("L3's sum : ", sum(L3))
print("L3's min : ", min(L3))
print("L3's max : ", max(L3))
