# https://leetcode.com/problems/jump-game/

'''
[T,T,T,F,F]
[2,3,1,1,4]
 ^ 
'''

def canJump(nums):
    if not nums:
        return False
    canReach = [False] * len(nums)
    canReach[0] = True
    for i, num in enumerate(nums):
        if canReach[i]:
            for j in range(num+1):
                if j + i < len(canReach):
                    canReach[j + i] = True
    return canReach[len(nums)-1]