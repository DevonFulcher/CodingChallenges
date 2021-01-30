
def canJump(nums):
    i = 0
    currMax = 0
    while i <= currMax:
        currMax = max(currMax, i+nums[i])
        i += 1
        if currMax >= len(nums)-1:
            return True
    return False
