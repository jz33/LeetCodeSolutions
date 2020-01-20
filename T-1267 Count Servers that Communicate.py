'''
1267. Count Servers that Communicate
https://leetcode.com/problems/count-servers-that-communicate/

You are given a map of a server center, represented as a m * n integer matrix grid,
where 1 means that on that cell there is a server and 0 means that it is no server.
Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example 2:

Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

Example 3:

Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
'''
from collections import defaultdict

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        colCount = len(grid[0])
    
        rowToCol = defaultdict(list)
        colToRow = defaultdict(list)
        total = 0
        for i in range(rowCount):
            for j in range(colCount):
                if grid[i][j] == 1:
                    rowToCol[i].append(j)
                    colToRow[j].append(i)
                    total += 1
        
        isolated = 0
        for i,ls in rowToCol.items():
            if len(ls) == 1:
                j = ls[0]
                if len(colToRow[j]) == 1:
                    isolated += 1
        
        return total - isolated
