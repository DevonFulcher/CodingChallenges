# https://algo.monster/problems/binary_search_first_element_not_smaller_than_target
from typing import List

def first_not_smaller(arr: List[int], target: int) -> int:
    if arr[0] > target:
        return 0
    
    l, r = 0, len(arr)-1
    mid = 0
    while l+1 < r:
        mid = ((r-l) // 2) + l
        if arr[mid] < target:
            l = mid
        elif arr[mid] >= target:
            r = mid
    return r