# Get List data
def get_float_List():
    L_float = list(map(float, input("Enter float : ").split(" ")))
    return L_float


# List Statistics
def get_statistics(L):
    yield len(L)  # length
    yield min(L)  # min
    yield max(L)  # max
    temp = 0  # to save L's sum
    for i in L:
        temp += i
    avg = temp / len(L)
    yield avg  # avg
    temp = 0  # to save (L's value - avg)^2's sum
    for i in L:
        temp += (i - avg)**2
    var = temp / len(L)
    yield var  # var
    yield var ** 0.5  # std = var ^ 0.5
    return 0


# Sort - Selection Sort
def sort_list(L):
    for i in range(len(L)):
        min = i
        for j in range(i, len(L)):
            if L[i] > L[j]:
                min = j
        # Swap
        temp = L[i]
        L[i] = L[min]
        L[min] = temp
    return L
