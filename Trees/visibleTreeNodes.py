# https://algo.monster/problems/visible_tree_node

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node) -> int:
    num_visible = 0
    def count_visible(node, max_so_far):
        nonlocal num_visible
        if not node:
            return
        if node.val >= max_so_far:
            num_visible += 1
        curr_max = max(max_so_far, node.val)
        count_visible(node.left, curr_max)
        count_visible(node.right, curr_max)
    count_visible(root, float("-inf"))
    return num_visible
