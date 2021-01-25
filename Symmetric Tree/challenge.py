class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: TreeNode) -> bool:

    if not root:
        return True

    def helper(l_tree, r_tree):
        if not l_tree and not r_tree:
            return True
        if not l_tree or not r_tree:
            return False
        return l_tree.val == r_tree.val and helper(l_tree.right, r_tree.left) and helper(l_tree.left, r_tree.right)

    return helper(root.left, root.right)


def isSymmetricIterative(root: TreeNode) -> bool:
    from collections import deque

    if not root:
        return True

    stack = deque([root.left, root.right])
    while stack:
        t1 = stack.pop()
        t2 = stack.pop()
        if not t1 and not t2:
            continue
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        stack.append(t2.left)
        stack.append(t1.right)
        stack.append(t2.right)
        stack.append(t1.left)
    return True
