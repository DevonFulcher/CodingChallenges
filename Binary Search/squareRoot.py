# https://algo.monster/problems/sqrt
def square_root(n: int) -> int:
    l, r = 1, n
    while l+1 < r:
        mid = ((r-l) // 2) + l
        if mid * mid > n:
            r = mid
        elif mid * mid < n:
            l = mid
        elif mid * mid == n:
            return mid
    if r * r == n:
        return r
    return l