#https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        str_lists = list(map(lambda a_str: list(a_str), strs))
        
        min_len = len(strs[0])
        for a_str in strs:
            if len(a_str) < min_len:
                min_len = len(a_str)
        
        common_prefix = []
        no_match = False
        for i in range(min_len):
            curr = str_lists[0][i]
            for j in range(len(strs)):
                if str_lists[j][i] != curr:
                    return "".join(common_prefix)
            common_prefix.append(curr)
        return "".join(common_prefix)