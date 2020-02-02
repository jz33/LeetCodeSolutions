'''
37. Sudoku Solver
https://leetcode.com/problems/sudoku-solver/

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

A sudoku puzzle...

...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
'''
class Solution:
    def isValid(self, x: int, y: int) -> bool:
        '''
        Check if newly added number on (x,y) is valid
        '''
        board = self.board
        
        # check row
        bitmap = 0
        for i in range(9):
            if board[x][i] != '.':
                n = int(board[x][i])
                bitmap = bitmap ^ (1 << n)
                if (bitmap & (1 << n)) == 0:
                    return False
                    
        # check column
        bitmap = 0
        for i in range(9):
            if board[i][y] != '.':
                n = int(board[i][y])
                bitmap = bitmap ^ (1 << n)
                if (bitmap & (1 << n)) == 0:
                    return False
     
        # check 3 * 3 submatrix
        bitmap = 0
        for i in range((x // 3) * 3, (x // 3) * 3 + 3):
            for j in range((y // 3) * 3, (y // 3) * 3 + 3):
                if board[i][j] != '.': 
                    n = int(board[i][j])
                    bitmap = bitmap ^ (1 << n)
                    if (bitmap & (1 << n)) == 0:
                        return False
               
        return True
        
    def backtrack(self, i: int) -> bool:
        if i == len(self.emptyCells):
            return True
        
        x,y = self.emptyCells[i]
        for n in range(1, 10):
            self.board[x][y] = str(n)
            if self.isValid(x, y) and self.backtrack(i+1):
                return True
            
        self.board[x][y] = '.'
        return False
                
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.emptyCells = [(i,j) for i in range(9) for j in range(9) if board[i][j] == '.']
        self.board = board
        self.backtrack(0)
