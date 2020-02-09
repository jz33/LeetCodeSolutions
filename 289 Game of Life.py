'''
289. Game of Life
https://leetcode.com/problems/game-of-life/

According to the Wikipedia's article: "The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using
the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.
The next state is created by applying the above rules simultaneously to every cell in the current state,
where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time:
You cannot update some cells first and then use their updated values to update other cells.

In this question, we represent the board using a 2D array.
In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array.
How would you address these problems?
'''
'''
0 : dead
1 : live
2 : live, was dead
3 : dead, was live
'''
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rowCount = len(board)
        colCount = len(board[0])

        # Change to live or dead
        for i in range(rowCount):
            for j in range(colCount):
                count = 0 # live neighbor count
                for x,y in (i, j+1), (i, j-1), (i+1, j), (i-1, j), (i+1, j+1), (i-1, j+1), (i+1, j-1), (i-1, j-1):
                    if 0 <= x < rowCount and 0 <= y < colCount and (board[x][y] & 1) == 1:
                        count += 1 # live neighbors include live at beginning or was live now dead
                        
                if board[i][j] > 0:
                    if count < 2 or count > 3:
                        # Dead due to under or over population
                        board[i][j] = 3
                        
                elif count == 3:
                    # Reproduction
                    board[i][j] = 2
        
        # Repaint board
        for i in range(rowCount):
            for j in range(colCount):
                e = board[i][j]
                if e == 2:
                    board[i][j] = 1
                elif e == 3:
                    board[i][j] = 0
