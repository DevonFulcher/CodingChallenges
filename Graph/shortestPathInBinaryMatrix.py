# https://leetcode.com/problems/shortest-path-in-binary-matrix/submissions/

from collections import deque

def get_neighbors(grid, x, y):
    neighbors = [
        (x+1, y),
        (x+1, y+1),
        (x+1, y-1),
        (x-1, y),
        (x-1, y+1),
        (x-1, y-1),
        (x, y+1),
        (x, y-1)
    ]
   
    condition = lambda coord: \
        coord[0] >= 0 and \
        coord[1] >= 0 and \
        coord[0] < len(grid) and \
        coord[1] < len(grid)
       
   
    return list(filter(condition, neighbors))

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        start = (0, 0, 1)
        visited = set([start])
        queue = deque([start])
        while queue:
            curr_x, curr_y, depth = queue.popleft()
            if (curr_x, curr_y) in visited or grid[curr_x][curr_y] == 1:
                continue
            visited.add((curr_x, curr_y))
            if (curr_x, curr_y) == (len(grid)-1, len(grid)-1):
                return depth
            for neighbor in get_neighbors(grid, curr_x, curr_y):
                next_tuple = (neighbor[0], neighbor[1], depth+1)
                queue.append(next_tuple)
        return -1