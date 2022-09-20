# Training While Iterator

L = list()
print("Input unsigned integers (-1 to End)")
x = int(input("Data : "))
while x >= 0:
    L.append(x)
    x = int(input("Data : "))
print("List L is : ", L)

A = list()
print("Input integers (-1 to End)")
while True:
    y = int(input("Data : "))
    if y == -1:
        break
    else:
        L.append(y)
        continue

print("List L is : ", L)