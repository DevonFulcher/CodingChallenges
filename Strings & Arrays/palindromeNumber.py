
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if abs(x) != x:
            return False
        x_str = str(x)
        l, r = 0, len(x_str)-1
        while l <= r:
            if x_str[l] != x_str[r]:
                return False
            l += 1
            r -= 1
        return True