'''
51 N-Queens
https://leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''
class Solution:
    def printBoard(self, board) -> List[str]:
        n = self.n
        out = [['.'] * n for _ in range(n)]
        for i in range(n):
            out[i][board[i]] = 'Q'
            
        return [''.join(out[i]) for i in range(n)]    
        
    def isValid(self, board, x, y) -> bool:
        # A new queen is just placed on (x, y), aka, board[x] = y
        # Only need to check previous queens in [0...x-1][0...y-1]
        # Notice previous queens cannot on same row as new queen
        # Iterate through previous rows
        for i in range(x):
            if board[i] == y:
                # A previous queen is in same column as the new queen
                return False
            if abs(i - x) == abs(board[i] - y):
                # A previous queen is in same diagnol as the new queen
                # aka, their row distance == column distance
                return False
        return True
    
    def backtrack(self, board, rowIndex):
        '''
        Try set a new queen row by row
        '''
        if rowIndex == self.n:
            self.pool.append(self.printBoard(board))
            return
        
        for i in range(self.n):
            # Try place queen on all columns on current row
            board[rowIndex] = i
            
            if self.isValid(board, rowIndex, i):
                # If valid, go further
                self.backtrack(board, rowIndex + 1)
            else:
                # otherwise, remove the queen
                board[rowIndex] = None
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.pool = []
        
        # A 1-D vector represents the 2-D board
        # If board[3] == 5, it means there is a queen on (3, 5)
        board = [None] * n
        self.backtrack(board, 0)
        return self.pool
