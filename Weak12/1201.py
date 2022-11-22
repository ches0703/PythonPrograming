# merge sort

def mergeSort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        midle = len(arr) // 2
        left = mergeSort(arr[:midle])
        right = mergeSort(arr[midle:])
        return merge(left, right)


def merge(left, right):
    arr_resulte = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr_resulte.append(left[i])
            i += 1
        else:
            arr_resulte.append(right[j])
            j += 1
    while i < len(left):
        arr_resulte.append(left[i])
        i += 1
    while j < len(right):
        arr_resulte.append(right[j])
        j += 1
    return arr_resulte


if __name__ == "__main__":
    arr = [2, 4, 6, 8, 3, 2, 1, 4, 6, 8, 4, 2, 0]
    after_sort_arr = mergeSort(arr)
    print(after_sort_arr)
