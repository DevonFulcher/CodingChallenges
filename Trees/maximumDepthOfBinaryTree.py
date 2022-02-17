# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    left_depth = maxDepth(root.left) + 1
    right_depth = maxDepth(root.right) + 1
    return max(left_depth, right_depth)

# iterative
from collections import deque
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    queue = deque([(1, root)])
    max_depth = 1
    while queue:
        depth, curr = queue.popleft()
        if not curr:
            continue
        max_depth = max(max_depth, depth)
        queue.append((depth + 1, curr.right))
        queue.append((depth + 1, curr.left))
    return max_depth
