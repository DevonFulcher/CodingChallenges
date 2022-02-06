# https://algo.monster/problems/binary_search_boundary
from typing import List

def find_boundary(arr: List[bool]) -> int:
    l, r = 0, len(arr)-1
    while l+1 < r:
        mid = (l+r) // 2
        if arr[mid] == False:
            l = mid
        elif arr[mid] == True:
            r = mid
    if arr[l] == False and arr[r] == True:
        return r
    elif arr[l] == True:
        return l
    else:
        return -1