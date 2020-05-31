# https://leetcode.com/problems/missing-number/solution/

def missingNumber(nums):
    targetValue = int(len(nums)*(len(nums)+1)/2)
    total = 0
    for num in nums:
        total += num
    return targetValue - total