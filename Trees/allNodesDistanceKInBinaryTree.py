# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        queue = deque([(None, root)])
        adjacencies = defaultdict(list)
        
        while queue:
            parent, node = queue.popleft()
            if parent:
                adjacencies[node.val].append(parent)
            if node.left:
                adjacencies[node.val].append(node.left)
                queue.append((node, node.left))
            if node.right:
                adjacencies[node.val].append(node.right)
                queue.append((node, node.right))
        
        queue = deque([(0, target)])
        visited = set([target.val])
        result = []
        while queue:
            depth, node = queue.popleft()
            visited.add(node.val)
            if depth == k:
                result.append(node.val)
            if depth > k:
                continue
            for neighbor in adjacencies[node.val]:
                if neighbor.val not in visited:
                    queue.append((depth+1, neighbor))
                
        return result