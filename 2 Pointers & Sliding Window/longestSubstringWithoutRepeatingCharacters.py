# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l, r = 0, 0
        max_length = 0
        while r < len(s):
            while s[r] not in chars:
                chars.add(s[r])
                r += 1
                if r >= len(s):
                    return max(max_length, len(chars))
            max_length = max(max_length, len(chars))
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
        return max_length