'''
Shorted Distance from All Buildings
https://leetcode.com/problems/shortest-distance-from-all-buildings/
'''
from Queue import Queue

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R = len(grid)
        if R == 0: return 0
        C = len(grid[0])

        #BFS
        INF = (R+C)*R*C
        directions = [0,1,0,-1,0]
        minDist = 0
        
        # recording all distances from each BFS 
        total_grid = [[0 for _ in xrange(C)] for _ in xrange(R)]
        
    
        # 0. Mark visited node; 1. Detect unreachable node
        walk = 0
        for i in xrange(R):
            for j in xrange(C):
                if grid[i][j] == 1:
                    # start BFS
                    # current distances reachable by current start point
                    dist_grid = [[0 for _ in xrange(C)] for _ in xrange(R)]
                    dq = Queue()
                    dq.put((i,j))
                    minDist = INF # for each BFS, minDist is reset
                    while not dq.empty():
                        a,b = dq.get()
                        dab = dist_grid[a][b]
                        for k in xrange(4):
                            x = a + directions[k]
                            y = b + directions[k+1]
                            if x > -1 and x < R and y > -1 and y < C and grid[x][y] == walk:
                                grid[x][y] -= 1 # mark as visited
                                d = dab + 1
                                dist_grid[x][y] = d
                                total_grid[x][y] += d
                                minDist = min(minDist,total_grid[x][y])
                                dq.put((x,y))
                    if minDist == INF: return -1
                    walk -= 1
        return minDist
        
        
sol = Solution()
grid = [
    [1,2,1],
    [0,0,0],
    [0,1,0]
    ]
print sol.shortestDistance(grid)
