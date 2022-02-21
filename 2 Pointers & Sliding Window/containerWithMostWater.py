# https://leetcode.com/problems/container-with-most-water/

def maxArea(height):
    leftPointer, rightPointer = 0, len(height)-1
    greatestArea = 0
    while leftPointer != rightPointer:
        greatestArea = max(greatestArea, min(
            height[leftPointer], height[rightPointer])*(rightPointer-leftPointer))
        if height[leftPointer] < height[rightPointer]:
            leftPointer += 1
        else:
            rightPointer -= 1
    return greatestArea
