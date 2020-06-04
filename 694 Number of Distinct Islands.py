'''
694. Number of Distinct Islands
https://leetcode.com/problems/number-of-distinct-islands/

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if
one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.

Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.

Note: The length of each dimension in the given grid does not exceed 50.
'''
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rowCount = len(grid)
        colCount = len(grid[0])
        visited = [[False] * colCount for _ in range(rowCount)]
        
        '''
        The idea is to do dfs search, and for each step record directions.
        For same shapes, dfs direcition paths should be identical.
        Valid directions are [0,1,2,3], and -1 is for delimiter.
        '''
        def dfs(i, j, direction, directionPath):
            nonlocal visited
            if 0 <= i < rowCount and 0 <= j < colCount and grid[i][j] == 1 and visited[i][j] == False:
                visited[i][j] = True
                directionPath.append(direction)
                
                for d, (x, y) in enumerate([(i+1, j), (i-1, j), (i, j+1), (i, j-1)]):
                    dfs(x, y, d, directionPath)
                
                # Must add a delimiter to distinguish different shapes!
                directionPath.append(-1)
                
        # Set of direction paths
        paths = set()
        for i in range(rowCount):
            for j in range(colCount):
                path = []
                dfs(i, j, -1, path)
                if path:
                    paths.add(tuple(path))

        return len(paths)
