# https://leetcode.com/problems/climbing-stairs/

def climbStairs(n):
    twoStepsBack = 0
    oneStepBack = 0
    currSteps = 0
    for i in range(n):
        currSteps = twoStepsBack + oneStepBack + 3
        twoStepsBack, oneStepBack = oneStepBack, currSteps
    return currSteps
