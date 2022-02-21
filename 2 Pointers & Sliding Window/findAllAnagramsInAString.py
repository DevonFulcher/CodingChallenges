from collections import deque, Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, r = 0, len(p)
        window_counter = Counter(deque(s[l:r]))
        result = []
        p_counter = Counter(p)
        while r < len(s):
            if window_counter == p_counter:
                result.append(l)
            window_counter[s[l]] -= 1
            window_counter[s[r]] += 1
            l += 1
            r += 1

        if window_counter == p_counter:
            result.append(l)
        return result