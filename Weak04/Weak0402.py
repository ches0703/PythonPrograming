# List

L = input().split(sep=" ")
print(L)
L = list(map(int, L))
print(L)
L.sort()
print(L)
print(L.pop())
L.remove(3)
print(L)
print(2 in L)