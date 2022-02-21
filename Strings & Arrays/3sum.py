# https://leetcode.com/problems/3sum
from typing import List

def two_sum(nums, start, result):
    end = len(nums)-1
    if start+1 == end:
        return
    mid = start+1
    start_sum = nums[start]
    while mid < end:
        curr = start_sum + nums[mid] + nums[end]
        if curr == 0:
            result.add((nums[start], nums[mid], nums[end]))
            mid += 1
        if curr < 0:
            mid += 1
        if curr > 0:
            end -= 1

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            two_sum(sorted_nums, i, result)
        return list(map(lambda triple: list(triple), list(result)))