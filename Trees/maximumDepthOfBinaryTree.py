# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    left_depth = maxDepth(root.left) + 1
    right_depth = maxDepth(root.right) + 1
    return max(left_depth, right_depth)
