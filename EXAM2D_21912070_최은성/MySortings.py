# MySortings.py
"""
Project :  EXAM2D MySortings
Author: Eun-seong Choi
Date of last update: 2022 / 12 / 11
Update list:
    - v1,1 : 12 /11
        Make funtion : quicSort
            _quickSortLoop, _partition
"""

# quick sort : partition & compare
def _partition(arr, left, right, pi):
    pv = arr[pi]
    arr[pi], arr[right] = arr[right], arr[pi]
    new_pi = i = left           # pivot value in left
    while (i<=right-1):
        if (arr[i] <= pv):
            arr[new_pi], arr[i] = arr[i], arr[new_pi] # SWAP : to smaller move to left
            new_pi += 1
        i += 1
    arr[new_pi], arr[right] = arr[right], arr[new_pi] # SWAP : for collect pivot set
    return new_pi

# loop by partion resulte
def _quickSortLoop(arr, left, right):
    if (left >= right):
        return
    pi = (left + right)//2
    new_pi = _partition(arr, left, right, pi)
    if (left < new_pi -1): 
        _quickSortLoop(arr, left, new_pi-1)  # pivot's left side
    if (new_pi + 1 < right): 
        _quickSortLoop(arr, new_pi+1, right)  # pivot's right side

# quicSort Start
def quickSort(arr):
    size = len(arr) 
    # sort range : left(0) to right(last in List)
    _quickSortLoop(arr, 0, size-1)