# https://leetcode.com/problems/symmetric-tree/
import collections

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = None

def isSymmetric(root):
    queue = collections.deque([root])
    thisLevel = []
    i = 0
    powerOfTwoExponent = 0
    while queue:
        currNode = queue.popleft()
        thisLevel.append(currNode.val)
        if currNode.left:
            queue.append(currNode.left)
        if currNode.right:
            queue.append(currNode.right)
        i += 1
        if i == 2 ** powerOfTwoExponent:
            powerOfTwoExponent += 1
            i = 0
            halfLevelLength = len(thisLevel)//2
            if thisLevel[:halfLevelLength] != thisLevel[halfLevelLength::-1]:
                return False
            thisLevel = []
    return True
