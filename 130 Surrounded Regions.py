'''
Surrounded Regions
https://leetcode.com/problems/surrounded-regions/

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''
from typing import Tuple

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowCount = len(board)
        if not rowCount:
            return
        
        colCount = len(board[0])
        if not colCount:
            return
        
        IsIsland = 'O'
        IsLand = 'X'
        # Notice inside the queue and pop out of queue cases are different.
        # if treat them all as visisted, there will be duplciates in queue!
        IsInsideQueue = 'Q'
        IsPoped = 'P'      
        def mark(cell: Tuple[int, int]):
            # Use a stack to replace queue, as order does not matter
            stack = [cell]
            while stack:
                x, y = stack.pop()
                board[x][y] = IsPoped
                if x + 1 <  rowCount and board[x+1][y] == IsIsland:
                    stack.append((x+1,y))
                    board[x+1][y] = IsInsideQueue
                if x > 0 and board[x-1][y] == IsIsland:
                    stack.append((x-1,y))
                    board[x-1][y] = IsInsideQueue
                if y + 1 < colCount and board[x][y+1] == IsIsland:
                    stack.append((x,y+1))
                    board[x][y+1] = IsInsideQueue
                if y > 0 and board[x][y-1] == IsIsland:
                    stack.append((x,y-1))
                    board[x][y-1] = IsInsideQueue
        
        # Go through border, if is '0', mark all adjacent cells as 'V'
        for i in range(rowCount):
            if board[i][0] == IsIsland:
                mark((i,0))
            if board[i][colCount-1] == IsIsland:
                mark((i,colCount-1))

        for i in range(1,colCount-1):
            if board[0][i] == IsIsland:
                mark((0,i))
            if board[rowCount-1][i] == IsIsland:
                mark((rowCount-1,i))
            
        # For island cell, mark it to land, as it is not connected to bound;
        # For cell who is connected to boundry island, mark it back to island
        for i in range(rowCount):
            for j in range(colCount):
                if board[i][j] == IsIsland:
                    board[i][j] = IsLand
                elif board[i][j] == IsPoped:
                    board[i][j] = IsIsland
