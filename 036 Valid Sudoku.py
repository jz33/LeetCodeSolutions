'''
36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

Example 1:

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.
'''
# 10 '1's, bit mask to check if a number appeared
DEFAULT_MASK = 0x3ff

def isCharValid(c: str, mask: int):
    if c == '.':
        return True, mask
    i = int(c)
    # Flip mask[i]
    mask ^= (1<<i)
    # If appears only once, mask[i] should be 0
    if (mask & (1<<i)) != 0:
        return False, mask
    return True, mask

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for r in range(9):
            mask = DEFAULT_MASK
            for c in range(9):
                char = board[r][c]
                isValid, mask = isCharValid(char, mask)
                if not isValid:
                    return False
    
        # Check columns
        for c in range(9):
            mask = DEFAULT_MASK
            for r in range(9):
                char = board[r][c]
                isValid, mask = isCharValid(char, mask)
                if not isValid:
                    return False

        # Check 3*3 cells
        for i in range(3):
            for j in range(3):
                mask = DEFAULT_MASK
                for r in range(i*3, i*3+3):
                    for c in range(j*3,j*3+3):
                        char = board[r][c]
                        isValid, mask = isCharValid(char, mask)
                        if not isValid:
                            return False

        return True

        