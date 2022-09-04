# https://leetcode.com/problems/valid-palindrome-ii/solution/


class Solution:
    def validPalindrome(self, s: str) -> bool:
        valid_left = True
        l, r = 0, len(s)-1
        skipped = False
        while l < r:
            if s[l] != s[r]:
                if skipped:
                    valid_left = False
                    break
                l += 1
                skipped = True
                continue
            l += 1
            r -= 1
        
        valid_right = True
        l, r = 0, len(s)-1
        skipped = False
        while l < r:
            if s[l] != s[r]:
                if skipped:
                    valid_right = False
                    break
                r -= 1
                skipped = True
                continue
            l += 1
            r -= 1
        
        return valid_left or valid_right