'''
Best Meeting Point
https://leetcode.com/problems/best-meeting-point/
'''
class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R = len(grid)
        if R == 0: return 0
        C = len(grid[0])
        
        # find all nodes
        nodes = []
        for i in xrange(R):
            for j in xrange(C):
                if grid[i][j] == 1:
                    nodes.append((i,j))
        
        # middle of rows
        # nodes.sort(key = lambda x : x[0])
        cr = nodes[len(nodes) / 2][0]
        
        # middle of columns
        nodes.sort(key = lambda x : x[1])
        cc = nodes[len(nodes) / 2][1]
        
        dist = 0
        for (x,y) in nodes:
            dist += abs(x - cr) + abs(y - cc)
        return dist
        
sol = Solution()
grid = [
    [1,0,1],
    [0,0,0],
    [0,1,0]
    ]
print sol.minTotalDistance(grid)
