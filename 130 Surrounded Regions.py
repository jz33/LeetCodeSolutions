'''
130.Surrounded Regions
https://leetcode.com/problems/surrounded-regions/

Given an m x n matrix board containing 'X' and 'O',
capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:

Input: board = [["X"]]
Output: [["X"]]

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is 'X' or 'O'
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rowCount = len(board)
        colCount = len(board[0])

        def mark(sx: int, sy: int):
            if board[sx][sy] != 'O':
                return
            row = [(sx, sy)]
            board[sx][sy] = 'V'
            while row:
                newRow = []
                for x, y in row:
                    for i, j in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                        if 0 <= i < rowCount and 0 <= j < colCount and board[i][j] == 'O':
                            board[i][j] = 'V'
                            newRow.append((i, j))
                row = newRow

        # 1. From the boundary 'O's, mark all connected 'O' as 'V'
        for r in range(rowCount):
            mark(r, 0)
            mark(r, colCount - 1)
        for c in range(colCount):
            mark(0, c)
            mark(rowCount-1, c)

        # 2. Mark all remaining 'O' to 'X'
        for r in range(rowCount):
            for c in range(colCount):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        # 3. Change back all 'V' to 'O':
        for r in range(rowCount):
            for c in range(colCount):
                if board[r][c] == 'V':
                    board[r][c] = 'O'
        
