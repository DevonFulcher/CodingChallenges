
'''
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 1 1 1





[[0], [1]]

looks good to me! we'll wrap up in 5-10mins
can you tell me the runtime of your solution?
makes sense
are there any trade offs by not using space?
input gets destroyed
exactly! make sure to vocalize that tradeoff before going down that road with your interviewer
time - m * n 
space - constant
https://leetcode.com/problems/maximal-square/
'''


def greatest_area(grid):
    #shallow copy = grid 
    #deep copies below:
    #new_grid = grid[:][:]
    #new_grid = grid.copy()
    max_len = 0
    if len(grid[0]) == 1:
        for i in range(0, len(grid)):
            if grid[i][0] == 1:
                return 1
        return 0
        
    if len(grid) == 1:
        for num in grid[0]:
            if num == 1:
                return 1
        return 0
    else:    
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if grid[i][j] == 1:
                    diag = grid[i-1][j-1]
                    left = grid[i][j-1]
                    up = grid[i-1][j]
                    min_val = min(diag, left, up)
                    grid[i][j] = min_val + 1
                    
                    if max_len < grid[i][j]:
                        max_len = grid[i][j]
                        
    return max_len * max_len
    
#grid = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]

if __name__ == "__main__":
    grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    print(greatest_area(grid))