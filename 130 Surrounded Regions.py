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
Isle = 'O'
Land = 'X'
Visited = 'V'

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rowCount = len(board)        
        colCount = len(board[0])
        
        def mark(i,j):
            nonlocal board
            stack = [(i,j)]
            board[i][j] = Visited
            while stack:
                x, y = stack.pop()
                for i,j in (x, y+1), (x, y-1), (x+1, y), (x-1, y):
                    if 0 <= i < rowCount and 0 <= j < colCount and board[i][j] == Isle:
                        stack.append((i,j))
                        board[i][j] = Visited
        
        # Go through border, if is '0', mark all adjacent cells as 'V'
        for i in range(rowCount):
            if board[i][0] == Isle:
                mark(i,0)
            if board[i][colCount-1] == Isle:
                mark(i,colCount-1)

        for i in range(colCount):
            if board[0][i] == Isle:
                mark(0,i)
            if board[rowCount-1][i] == Isle:
                mark(rowCount-1,i)
            
        # For island cell, mark it to land, as it is not connected to bound;
        # For cell who is connected to boundry island, mark it back to island
        for i in range(rowCount):
            for j in range(colCount):
                if board[i][j] == Isle:
                    board[i][j] = Land
                elif board[i][j] == Visited:
                    board[i][j] = Isle
