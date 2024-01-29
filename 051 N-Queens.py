'''
51 N-Queens
https://leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that
no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:

Input: n = 1
Output: [["Q"]]

Constraints:
    1 <= n <= 9
'''
from typing import List
class Solution:      
    def solveNQueens(self, boardSize: int) -> List[List[str]]:
        pool = []

        def serializeBoard(board: List[int]) -> List[str]:
            out = [['.'] * boardSize for _ in range(boardSize)]
            for i in range(boardSize):
                out[i][board[i]] = 'Q'
            return [''.join(out[i]) for i in range(boardSize)]  

        def isValid(board: List[int], r: int, c: int) -> bool:
            # A new queen is just placed on (r, c), aka, board[r] = c
            # Check previous columns and diagonals
            for i in range(r):
                if board[i] == c:
                    # A previous queen is in same column as the new queen
                    return False
                if abs(i - r) == abs(board[i] - c):
                    # A previous queen is in same diagonal as the new queen
                    # aka, their row distance == column distance
                    return False
            return True 
    
        def backtrack(board: List[int], row: int):
            if row == boardSize:
                pool.append(serializeBoard(board))
                return
            
            # Try place a queen row by row
            for col in range(boardSize):
                # Try place queen on all columns on current row
                board[row] = col
                
                if isValid(board, row, col):
                    # If valid, go further
                    backtrack(board, row + 1)
                else:
                    # otherwise, remove the queen
                    board[row] = None

        # A 1-D vector represents the 2-D board
        # If board[3] == 5, it means there is a queen on (3, 5)
        # If board[4] == None, it means no queen on row 4
        initialBoard = [None] * boardSize
        backtrack(initialBoard, 0)
        return pool
