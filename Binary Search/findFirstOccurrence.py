# https://algo.monster/problems/binary_search_duplicates
from typing import List

def find_first_occurrence(arr: List[int], target: int) -> int:
    l, r = 0, len(arr)-1
    while l+1 < r:
        mid = ((r-l) // 2) + l
        if arr[mid] >= target:
            r = mid
        elif arr[mid] < target:
            l = mid
    if arr[l] == target:
        return l
    if arr[r] == target:
        return r
    return -1