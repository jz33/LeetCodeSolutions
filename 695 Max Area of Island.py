from collections import deque
'''
https://leetcode.com/problems/max-area-of-island
'''
def dfs(grid,R,C,i,j):    
    area = 0
    grid[i][j] = 2 # mark before push to deque
    dq = deque()
    dq.append((i,j))
    while len(dq) > 0:
        x,y = dq.popleft()
        area += 1     
        if x+1 < R and grid[x+1][y] == 1:
            grid[x+1][y] = 2
            dq.append((x+1,y))
        if x-1 >-1 and grid[x-1][y] == 1: 
            grid[x-1][y] = 2
            dq.append((x-1,y))
        if y+1 < C and grid[x][y+1] == 1: 
            grid[x][y+1] = 2
            dq.append((x,y+1))
        if y-1 >-1 and grid[x][y-1] == 1:
            grid[x][y-1] = 2
            dq.append((x,y-1))
    return area

def maxAreaOfIsland(grid):
    maxArea = 0
    R = len(grid)
    C = len(grid[0])
    for i in xrange(R):
        for j in xrange(C):
            if grid[i][j] == 1:
                area = dfs(grid,R,C,i,j)
                maxArea = max(maxArea, area)
    return maxArea
