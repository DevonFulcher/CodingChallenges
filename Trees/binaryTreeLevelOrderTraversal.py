# https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: TreeNode) -> list[list[int]]:
    if not root:
        return None

    result: list[list[int]] = []
    queue: deque[tuple[TreeNode, int]] = deque(
        [(root, 0)]  # current node, depth
    )
    while queue:
        node, depth = queue.pop()
        if not node:
            continue
        if len(result)-1 < depth:
            result.append([])
        level = result[len(result)-1]
        level.append(node.val)
        queue.appendleft((node.left, depth+1))
        queue.appendleft((node.right, depth+1))
    return result
