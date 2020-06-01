# https://leetcode.com/problems/minimum-path-sum/


class Node:
    def __init__(self, value, index):
        self.value = value
        self.index = index # (x, y) 2-tuple

def priorityInsert(nodeList, node):
    for i, listNode in enumerate(nodeList):
        if listNode.value < node.value:
            nodeList.insert(i, node)
            return
    nodeList.push(node)
    return
'''
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

priorityQueue = [Node(1,(0,0))]
'''

def minPathSum(grid):
    height, width = len(grid), len(grid[0])
    if height == 0 or width == 0:
        return 0
    priorityQueue = [] # list of Nodes in descending order by Node value
    firstNode = Node(grid[0][0], (0, 0))
    priorityInsert(priorityQueue, firstNode)
    visited = set() # set of visited (x, y) coordinates
    visited.add((0, 0))
    answer = 0
    while True:
        currNode = priorityQueue.pop()
        answer += currNode.value
        if currNode.index[0] == width and currNode.index[1] == height:
            return answer
        neighbors = [
            (currNode.index[0]-1, currNode.index[1])
            (currNode.index[0]+1, currNode.index[1])
            (currNode.index[0], currNode.index[1]-1)
            (currNode.index[0], currNode.index[1]+1)
        ]
        for neighbor in neighbors:
            newX, newY = neighbor[0], neighbor[1]
            if newX < width and newX >= 0 and newY < height and newY >= 0 and (newX, newY) not in visited:
                priorityInsert(priorityQueue, Node(grid[newX][newY], (newX, newY)))
                visited.add((newX, newY))
