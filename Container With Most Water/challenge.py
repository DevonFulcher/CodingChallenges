# https://leetcode.com/problems/container-with-most-water/

def naiveMaxArea(height):
    greatestArea = 0
    for i, val in enumerate(height):
        for j in range(i+1, len(height)):
            minHeight = min(val, height[j])
            greatestArea = max(greatestArea, minHeight * (j - i))
    return greatestArea

def maxArea(height):
    leftPointer, rightPointer = 0, len(height)-1
    greatestArea = 0
    while leftPointer != rightPointer:
        greatestArea = max(greatestArea, min(height[leftPointer], height[rightPointer])*(rightPointer-leftPointer))
        if height[leftPointer] < height[rightPointer]:
            leftPointer += 1
        else:
            rightPointer -= 1
    return greatestArea
    
print(naiveMaxArea([1,8,6,2,5,4,8,3,7]))
print(naiveMaxArea([1,2]))

print(naiveMaxArea([0,1]))