# https://leetcode.com/problems/two-sum/

'''
target = 9
nums = [2, 7, 11, 15]
'''

def twoSums(nums, target):
    numToIndex = {}
    for i, num in enumerate(nums):
        numToIndex[num] = i
    for i, num in enumerate(nums):
        if target-num in numToIndex and i != numToIndex[target-num]:
            return [i, numToIndex[target-num]]