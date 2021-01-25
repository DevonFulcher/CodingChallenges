# https://leetcode.com/problems/binary-tree-inorder-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode) -> list[int]:
    result = []

    def traverse(node: TreeNode):
        if node:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)

    traverse(root)
    return result


def inorderTraversalIteratively(root: TreeNode) -> list[int]:
    from collections import deque
    result = []
    curr = root
    stack = deque()
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result
