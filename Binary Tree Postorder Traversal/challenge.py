# https://leetcode.com/problems/binary-tree-postorder-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root: TreeNode) -> list[int]:
    result = []

    def traverse(node: TreeNode):
        if node:
            traverse(node.left)
            traverse(node.right)
            result.append(node.val)

    traverse(root)
    return result
