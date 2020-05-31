# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

'''
place all elements in a min heap. pop off k elements from the min heap
dfs left side of bst, pushing each node into the heap, otherwise stop when all nodes are in heap
'''

import heapq

def kthSmallest(root, k):
    heap = []
    heapq.heappush(heap, root.val)
    def dfs(node):
        if (node.left):
            heapq.heappush(heap, node.left.val)
            dfs(node.left)
        if (node.right):
            heapq.heappush(heap, node.right.val)
            dfs(node.right)
    dfs(root)
    return heapq.nsmallest(k, heap)[0]

