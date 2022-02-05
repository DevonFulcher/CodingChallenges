class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque, defaultdict
from typing import List

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        column_dict = defaultdict(list)
        
        queue = deque([(0, root)])
        min_column = max_column = 0
        while queue:
            column, node = queue.popleft()
            min_column = min(min_column, column)
            max_column = max(max_column, column)
            column_dict[column].append(node.val)
            if node.left:
                queue.append((column-1, node.left))
            if node.right:
                queue.append((column+1, node.right))
        
        result = []
        for i in range(min_column, max_column+1):
            result.append(column_dict[i])
            
        return result