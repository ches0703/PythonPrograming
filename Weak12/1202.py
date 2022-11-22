# Quick sorting

def partition(arr, left, right, pi):
    print(left, right, pi)
    pv = arr[pi]
    arr[pi], arr[right] = arr[right], arr[pi]
    new_pi = i = left
    while (i <= right - 1):
        if (arr[i] <= pv):
            arr[new_pi], arr[i] = arr[i], arr[new_pi]
            new_pi += 1
        i += 1
    arr[new_pi], arr[right] = arr[right], arr[new_pi]
    return new_pi


def quickSortLoop(arr, left, right):
    if (left >= right):
        return
    pi = (left + right) // 2
    new_pi = partition(arr, left, right, pi)
    if (left < new_pi - 1):
        quickSortLoop(arr, 0, new_pi - 1)
    if (new_pi + 1 < right):
        quickSortLoop(arr, new_pi + 1, right)


def quickSort(arr):
    quickSortLoop(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    arr = [4, 2, 1, 4, 5, 7]
    print(arr)
    quickSort(arr)
    print(arr)
