'''
827. Making A Large Island
https://leetcode.com/problems/making-a-large-island/

In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

Example 1:

Input: [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:

Input: [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:

Input: [[1, 1], [1, 1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
'''
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        '''
        First count all islands. Give each island an index,
        mark all nodes of that island to that index.
        Have an {island index : area} dict.
        Second go though all 0s, see if it connects any 
        islands.
        '''
        rowCount = len(grid)
        colCount = len(grid[0])
        
        # Build {island index : area}
        # island index starts from 2
        indexToArea = [0,0] 
        for i in range(rowCount):
            for j in range(colCount):
                if grid[i][j] == 1:
                    # BFS to mark grid and count area
                    area = 1
                    index = len(indexToArea)
                    grid[i][j] = index
                    stack = [(i,j)]
                    while stack:
                        x,y = stack.pop()
                        for a,b in (x,y+1), (x,y-1), (x+1,y), (x-1,y):
                            if 0 <= a < rowCount and 0 <= b < colCount and grid[a][b] == 1:
                                area += 1
                                stack.append((a,b))
                                grid[a][b] = index
                    indexToArea.append(area)
        
        # Go though 0s
        maxArea = max(indexToArea)
        for x in range(rowCount):
            for y in range(colCount):
                if grid[x][y] == 0:
                    islandIndexes = set()
                    for a,b in (x,y+1), (x,y-1), (x+1,y), (x-1,y):
                        if 0 <= a < rowCount and 0 <= b < colCount:
                            islandIndexes.add(grid[a][b])
                    area = sum(indexToArea[i] for i in islandIndexes) + 1
                    maxArea = max(maxArea, area)
                    
        return maxArea
