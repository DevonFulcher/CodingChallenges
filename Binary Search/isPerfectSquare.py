# https://leetcode.com/problems/valid-perfect-square/
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l, r = 1, num
        while l+1 < r:
            mid = ((r-l) // 2) + l
            if mid * mid > num:
                r = mid
            elif mid * mid < num:
                l = mid
            elif mid * mid == num:
                return True
        if r * r == num:
            return True
        return False