'''
Number of Islands
https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

DFS, same method to 130 Surrounded Regions 
'''
from typing import Tuple

WATER = '0'
LAND = '1'
VISITED = '2'

class Solution:
    def numIslands(self, board: List[List[str]]) -> int:
        rowCount = len(board)
        if rowCount == 0:
            return 0
        
        colCount = len(board[0])
        
        def mark(cell: Tuple[int, int]):
            stack = [cell]
            while stack:
                x, y = stack.pop()
                board[x][y] = VISITED
                if x + 1 <  rowCount and board[x+1][y] == LAND:
                    stack.append((x+1,y))
                if x - 1 > -1 and board[x-1][y] == LAND:
                    stack.append((x-1,y))
                if y + 1 < colCount and board[x][y+1] == LAND:
                    stack.append((x,y+1))
                if y - 1 > -1 and board[x][y-1] == LAND:
                    stack.append((x,y-1))
                  
        # Iterate though all lands
        islandsCount = 0
        for i in range(rowCount):
            for j in range(colCount):
                if board[i][j] == LAND:
                    mark((i,j))
                    islandsCount += 1
        
        return islandsCount
