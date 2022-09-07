# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/submissions/

from collections import Counter
from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if not words:
            return []
        i = 0
        while i+1 < len(words):
            if Counter(words[i]) == Counter(words[i+1]):
                del words[i+1]
                continue
            i += 1
        return words