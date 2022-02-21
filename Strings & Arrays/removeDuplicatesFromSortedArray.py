#https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
from collections import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        if len(nums) == 2:
            if nums[0] == nums[1]:
                del nums[1]
            return len(nums)
        l, r = 0, 1
        while r < len(nums):
            while nums[r] == nums[l]:
                del nums[r]
                if r >= len(nums):
                    return len(nums)
            l += 1
            r += 1
        return len(nums)