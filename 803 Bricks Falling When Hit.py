'''
803. Bricks Falling When Hit
https://leetcode.com/problems/bricks-falling-when-hit/

We have a grid of 1s and 0s; the 1s in a cell represent bricks.
A brick will not drop if and only if it is directly connected to the top of the grid,
or at least one of its (4-way) adjacent bricks will not drop.

We will do some erasures sequentially. Each time we want to do the erasure at the location (i, j),
the brick (if it exists) on that location will disappear, and then some other bricks may drop because of that erasure.

Return an array representing the number of bricks that will drop after each erasure in sequence.

Example 1:
Input: 
grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]
Output: [2]
Explanation: 
If we erase the brick at (1, 0), the brick at (1, 1) and (1, 2) will drop. So we should return 2.

Example 2:
Input: 
grid = [[1,0,0,0],[1,1,0,0]]
hits = [[1,1],[1,0]]
Output: [0,0]
Explanation: 
When we erase the brick at (1, 0), the brick at (1, 1) has already disappeared due to the last move.
So each erasure will cause no bricks dropping.  Note that the erased brick (1, 0) will not be counted as a dropped brick.
 
Note:

The number of rows and columns in the grid will be in the range [1, 200].
The number of erasures will not exceed the area of the grid.
It is guaranteed that each erasure will be different from any other erasure, and located inside the grid.
An erasure may refer to a location with no brick - if it does, no bricks drop.
'''

Root = (-1,-1)

class UnionFind:
    def __init__(self):
        # {node : parent node}
        self.parents = {Root : Root} 

        # {node : node count including self and all children}
        self.sizes = collections.Counter({Root : 0}) 

    def addNode(self, i):
        self.parents[i] = i
        self.sizes[i] = 1

    def find(self, i):
        parents = self.parents   
        if parents[i] != i:
            parents[i] = self.find(parents[i])
        return parents[i]

    def union(self, i, j):
        ri = self.find(i)
        rj = self.find(j)      
        if ri != rj:
            
            # Prefer to attach to root
            if ri == Root:
                self.parents[rj] = ri
                self.sizes[ri] += self.sizes[rj]
            else:
                self.parents[ri] = rj
                self.sizes[rj] += self.sizes[ri]

    def bricks(self):
        '''
        Get number of nodes whose attached to Root
        '''
        return self.sizes[Root]

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        if not grid or not grid[0]:
            return [0] * len(hits)

        rowCount = len(grid)
        colCount = len(grid[0])
        graph = UnionFind()

        def unionNeighbors(i,j):
            for x, y in (i, j+1), (i, j-1), (i+1, j), (i-1, j):
                if 0 <= x < rowCount and 0 <= y < colCount and grid[x][y] == 1:
                    graph.union((i,j), (x,y))

            if i == 0:
                graph.union((i,j), Root)

        # Initialize graph
        for i in range(rowCount):
            for j in range(colCount):
                if grid[i][j] == 1:
                    graph.addNode((i,j))

        # Mark hitted cells to 2
        for x, y in hits:
            if grid[x][y] == 1:
                grid[x][y] = 2

        # Union
        for i in range(rowCount):
            for j in range(colCount):
                if grid[i][j] == 1:
                    unionNeighbors(i,j)

        # Add back nodes from reversed hits
        res = []
        for x, y in reversed(hits):
            if grid[x][y] != 2:
                res.append(0)
            else:
                grid[x][y] = 1

                bricks = graph.bricks()
                unionNeighbors(x,y)
                newBricks = graph.bricks()

                res.append(max(newBricks - bricks - 1, 0))

        return res[::-1]
