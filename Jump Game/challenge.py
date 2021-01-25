
'''
[2,3,1,1,4]
 ^
currMax = 2
[1,0,1,0]
'''

def canJump(nums):
    i=0
    currMax = 0
    while i <= currMax:
        currMax = max(currMax, i+nums[i])
        i += 1
        if currMax >= len(nums)-1:
            return True
    return False