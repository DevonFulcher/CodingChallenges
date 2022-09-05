# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(nums, left, right, target):
            while left+1 < right:
                mid = (left+right)//2
                if nums[mid] > target:
                    right = mid
                elif nums[mid] < target:
                    left = mid
                else:
                    return mid
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            return -1
        
        l, r = 0, len(nums)-1
        while l+1 < r:
            mid = (l+r)//2
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
        
        if target >= nums[r] and target <= nums[-1]:
            return binary_search(nums, r, len(nums)-1, target)
        return binary_search(nums, 0, l, target)