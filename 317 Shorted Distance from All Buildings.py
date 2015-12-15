from collections import deque

def dump(mat):
    for row in mat:
        print row

'''
Shorted Distance from All Buildings
https://leetcode.com/problems/shortest-distance-from-all-buildings/
'''
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R = len(grid)
        if R == 0: return 0
        C = len(grid[0])

        INF = (R+C)*R*C
        directions = [0,1,0,-1,0]
        minDist = 0
        total_grid = [[0 for _ in xrange(C)] for _ in xrange(R)]
        
        '''
        0. Mark visited node; 1. Detect unreachable node
        '''
        walk = 0
        for i in xrange(R):
            for j in xrange(C):
                if grid[i][j] == 1:
                    dist_grid = [[0 for _ in xrange(C)] for _ in xrange(R)]
                    dq = deque()
                    dq.append((i,j))
                    minDist = INF
                    while len(dq) > 0:
                        (a,b) = dq.popleft()
                        dab = dist_grid[a][b]
                        for k in xrange(4):
                            x = a + directions[k]
                            y = b + directions[k+1]
                            if x > -1 and x < R and y > -1 and y < C and grid[x][y] == walk:
                                grid[x][y] -= 1
                                d = dab + 1
                                dist_grid[x][y] = d
                                total_grid[x][y] += d
                                minDist = min(minDist,total_grid[x][y])
                                dq.append((x,y))
                    if minDist == INF: return -1
                    walk -= 1
        dump(grid)                
        dump(total_grid)
        return minDist
        
sol = Solution()
grid = [
    [1,2,1],
    [0,0,0],
    [0,1,0]
    ]
print sol.shortestDistance(grid)
