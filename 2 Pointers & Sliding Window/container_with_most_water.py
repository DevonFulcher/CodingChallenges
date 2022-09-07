# https://leetcode.com/problems/container-with-most-water/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_area = 0
        while l < r:
            curr_height = min(height[l], height[r])
            area = curr_height * (r - l)
            max_area = max(area, max_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area