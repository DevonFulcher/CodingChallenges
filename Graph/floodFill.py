# https://leetcode.com/problems/flood-fill

from collections import deque
from typing import List

def get_neighbors(image, x, y):
    neighbors = [
        (x+1, y),
        (x-1, y),
        (x, y+1),
        (x, y-1)
    ]
   
    condition = lambda coord: \
        coord[0] >= 0 and \
        coord[1] >= 0 and \
        coord[0] < len(image) and \
        coord[1] < len(image[0])
   
    return list(filter(condition, neighbors))

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        start = (sr, sc)
        queue = deque([start])
        visited = set()
        prev_color = image[sr][sc]
        while queue:
            curr_x, curr_y = queue.popleft()
            if (curr_x, curr_y) in visited or image[curr_x][curr_y] != prev_color:
                continue
            visited.add((curr_x, curr_y))
            image[curr_x][curr_y] = newColor
            for neighbor in get_neighbors(image, curr_x, curr_y):
                queue.append(neighbor)
        return image