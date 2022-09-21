# Sequence Data Type

# List

import copy

L0 = []
L0 = list()
L0 = [1, 2, 3]
L0 = list(range(3))

L1 = [1, 2, 3]
L2 = [3, 4, 5]
L3 = L1 + L2
print(L3)
print(L1 * 3)
print(0 in L1)
print(0 not in L2)
print(min(L1))
print(max(L1))

L4 = [7, 3, 10, 5, 1, 2, 4, 8]
L4 = sorted(L4)
print(sum(L4))
print(len(L4))
print(L4)
del (L4[4])
print(L4)

L5 = L4[0:5]
print(L5)
del L5[0:4]
print(L5)

L6 = [x for x in range(10)]
print(L6)
L7 = [x for x in 'abcda']
print(L7)
print(L7.count('a'))
print(L7.index('a'))
print(L7[-1])

L8 = [1, 2, 3]
L9 = L8
L8.append(4)
print(L8)
print(L9)

L8.clear()
print(L8)
print(L9)

L8 = [1, 2, 3, 4]
L9 = copy.deepcopy(L8)
L8.append(5)
print(L8)
print(L9)

L10 = [1, 2, 3]
L11 = [4, 5, 6]
L12 = [7, 8, 9]
L10.append(L11)
L10.extend(L12)
print(L10)

L13 = [1, 2, 3, 4, 5]
L13.insert(1, 1.5)
print(L13)
L13.pop()
print(L13)
L13.pop(1)
print(L13)
L13.remove(4)
print(L13)
L13.reverse()
print(L13)

L_A = [True, True, False]
print(any(L_A))
print(all(L_A))

L_colors = ["red", "blud", "purple", "green", ]
L_colors = sorted(L_colors)
print(L_colors)
