# https://leetcode.com/problems/first-bad-version/

def firstBadVersion(n):
    left, right = 0, n
    mid = n//2
    while True:
        if mid == n:
            return n
        leftVersion = isBadVersion(mid)
        rightVersion = isBadVersion(mid+1)
        if not leftVersion and rightVersion:
            return rightVersion
        if leftVersion:
            mid = mid//2
        else:
            mid = (n-mid)//2+mid
    return mid+1
