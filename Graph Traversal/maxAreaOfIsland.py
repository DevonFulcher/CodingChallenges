# https://leetcode.com/problems/max-area-of-island/

from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        visited = set()

        def get_neighbors(i, j):
            possible_neighbors = [
                (i+1, j),
                (i-1, j),
                (i, j+1),
                (i, j-1)
            ]

            return list(filter(
                lambda pos:
                    pos[0] >= 0 and
                    pos[1] >= 0 and
                    pos[0] < len(grid) and
                    pos[1] < len(grid[0]),
                possible_neighbors
            ))

        def bfs_max_area(start_i, start_j):
            island_area = 0
            queue = deque([(start_i, start_j)])
            while queue:
                curr_i, curr_j = queue.pop()
                curr_elem = grid[curr_i][curr_j]
                if curr_elem != 1 or (curr_i, curr_j) in visited:
                    continue
                island_area += 1
                visited.add((curr_i, curr_j))
                neighbors = get_neighbors(curr_i, curr_j)
                for neighbor in neighbors:
                    queue.appendleft(neighbor)
            return island_area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                island_area = bfs_max_area(i, j)
                max_area = max(island_area, max_area)

        return max_area
