# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        top = [1 for _ in range(n)]
        paths_grid = [top]
        for i in range(1, m):
            curr_path_row = []
            for j in range(n):
                if j == 0:
                    curr_path_row.append(1)
                else:
                    curr_path_row.append(paths_grid[i-1][j] + curr_path_row[j-1])
            paths_grid.append(curr_path_row)
        return paths_grid[m-1][n-1]