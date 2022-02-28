# https://leetcode.com/problems/merge-intervals/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda i: i[0])
        i = 0
        while i < len(sorted_intervals)-1:
            if sorted_intervals[i][1] >= sorted_intervals[i+1][0]:
                sorted_intervals[i][1] = max(sorted_intervals[i][1], sorted_intervals[i+1][1])
                del sorted_intervals[i+1]
            else:
                i += 1
        return sorted_intervals