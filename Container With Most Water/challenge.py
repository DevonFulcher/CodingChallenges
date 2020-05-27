# https://leetcode.com/problems/container-with-most-water/

def naiveMaxArea(height):
    greatestArea = 0
    for i, val in enumerate(height):
        for j in range(i+1, len(height)):
            minHeight = min(val, height[j])
            greatestArea = max(greatestArea, minHeight * (j - i))
    return greatestArea

print(naiveMaxArea([1,8,6,2,5,4,8,3,7]))
print(naiveMaxArea([1,2]))

print(naiveMaxArea([0,1]))