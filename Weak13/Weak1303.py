# yield from

def getListUpDown(n) -> int:
    yield from range(n)
    yield from range(n, 0, -1)


L = list(getListUpDown(5))
print(L)

# Generator Expression

genList = (x * x for x in range(5))
print("genList : ", genList)
L = list(genList)
print(L)

