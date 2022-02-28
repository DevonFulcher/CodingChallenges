# https://leetcode.com/problems/house-robber/submissions/

from typing import List

class Solution:
   
    def rob(self, nums: List[int]) -> int:
        prev = 0
        prev_prev = 0
        curr = 0
        for i in range(len(nums)):
            curr = max(prev, prev_prev+nums[i])
            prev_prev = prev
            prev = curr
        return curr