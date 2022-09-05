# https://algo.monster/problems/knight_shortest_path

from collections import deque

def get_knight_shortest_path(x: int, y: int) -> int:
    def get_neighbors(curr_x, curr_y):
        return [
            (curr_x+2, curr_y-1),
            (curr_x+2, curr_y+1),
            (curr_x+1, curr_y-2),
            (curr_x+1, curr_y+2),
            (curr_x-1, curr_y-2),
            (curr_x-1, curr_y+2),
            (curr_x-2, curr_y-1),
            (curr_x-2, curr_y+1)
        ]
    
    queue = deque([(x, y, 0)])
    while queue:
        curr_x, curr_y, depth = queue.pop()
        if curr_x == 0 and curr_y == 0:
            return depth
        for neighbor_x, neighbor_y in get_neighbors(curr_x, curr_y):
            queue.appendleft((neighbor_x, neighbor_y, depth+1))