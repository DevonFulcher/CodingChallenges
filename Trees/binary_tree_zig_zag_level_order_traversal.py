# https://algo.monster/problems/binary_tree_zig_zag_traversal

from typing import List
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zig_zag_traversal(root: Node) -> List[List[int]]:
    result = []
    queue = deque([(root, 0)])
    while queue:
        curr, level = queue.popleft()
        if not curr:
            continue
        if level > len(result)-1:
            result.append(deque([]))
        if level % 2 == 1:
            result[level].append(curr.val)
        else:
            result[level].appendleft(curr.val)
        queue.append((curr.right, level+1))
        queue.append((curr.left, level+1))
    return result
    