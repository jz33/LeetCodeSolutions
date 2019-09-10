'''
Surrounded Regions
https://leetcode.com/problems/surrounded-regions/
'''
from typing import Tuple

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowCount = len(board)
        if rowCount == 0:
            return
        
        colCount = len(board[0])
        
        def mark(cell: Tuple[int, int]):
            stack = [cell]
            while stack:
                x, y = stack.pop()
                board[x][y] = 'V'
                if x + 1 <  rowCount and board[x+1][y] == 'O':
                    stack.append((x+1,y))
                if x - 1 > -1 and board[x-1][y] == 'O':
                    stack.append((x-1,y))
                if y + 1 < colCount and board[x][y+1] == 'O':
                    stack.append((x,y+1))
                if y - 1 > -1 and board[x][y-1] == 'O':
                    stack.append((x,y-1))
        
        # Go through border, if is '0', mark all adjacent cells as 'V'
        for i in range(rowCount):
            if board[i][0] == 'O':
                mark((i,0))
            if board[i][colCount-1] == 'O':
                mark((i,colCount-1))

        for i in range(1,colCount-1):
            if board[0][i] == 'O':
                mark((0,i))
            if board[rowCount-1][i] == 'O':
                mark((rowCount-1,i))
            
        # For all cells with 'O', mark it to 'X'
        # For all cells with 'V', mark it back to 'O'
        for i in range(rowCount):
            for j in range(colCount):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'V':
                    board[i][j] = 'O'
