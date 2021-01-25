# https://leetcode.com/problems/validate-binary-search-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: TreeNode) -> bool:

    def helper(node: TreeNode, min_val, max_val):
        if node:
            return node.val < max_val and \
                node.val > min_val and \
                helper(node.left, min_val, node.val) and \
                helper(node.right, node.val, max_val)
        return True

    return helper(root, float("-inf"), float("inf"))
