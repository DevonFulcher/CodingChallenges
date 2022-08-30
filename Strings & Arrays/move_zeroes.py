# https://leetcode.com/problems/move-zeroes/
from typing import List

def move_zeroes(nums: List[int]) -> None:
    count = 0
    for i in enumerate(nums):
        nums[i-count] = nums[i]
        if nums[i] == 0:
            count += 1
    for i in range(1, count+1):
        nums[-i] = 0
        