'''
773. Sliding Puzzle
https://leetcode.com/problems/sliding-puzzle/

On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved.
If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.

Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]

Input: board = [[3,2,4],[1,5,0]]
Output: 14

Note:

board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
'''
from collections import deque
from typing import Tuple

class Solution:
    def findZero(self, tb: Tuple[int])-> int:
        for i in range(6):
            if tb[i] == 0:
                return i
            
    def getNewBoard(self, tb: Tuple[int], zi: int):
        '''
        Return new board of 1 0 movement
        @tb: tupled board
        @zi: current zero index
        '''
        board = list(tb)
        res = []
        
        if zi != 0 and zi != 3:
            # swap 0 with left
            board[zi],board[zi-1] = board[zi-1],board[zi]
            res.append((tuple(board), zi-1))
            board[zi],board[zi-1] = board[zi-1],board[zi]
        if zi != 2 and zi != 5:
            # swap 0 with right
            board[zi],board[zi+1] = board[zi+1],board[zi]
            res.append((tuple(board), zi+1))
            board[zi],board[zi+1] = board[zi+1],board[zi]
        if zi < 3:
            # swap 0 down
            board[zi],board[zi+3] = board[zi+3],board[zi]
            res.append((tuple(board), zi+3))
        else: # 3 <= z < 6
            # swap 0 up
            board[zi],board[zi-3] = board[zi-3],board[zi]
            res.append((tuple(board), zi-3))

        return res
  
    def slidingPuzzle(self, board: List[List[int]]) -> int:    
        # Queue records board and position of 0
        # Notice the board is flatten to tuple of 6 for hashing
        queue = deque()
        tb = tuple(board[0] + board[1])
        queue.append((tb, self.findZero(tb)))
        
        # Records the visited board. Use tuple for hashing and comparison
        visited = set()
        visited.add(tb)
        
        depth = 0
        while queue:
            for _ in range(len(queue)):             
                tb, zi = queue.popleft()
                if tb == (1,2,3,4,5,0):
                    return depth
                
                for b,z in self.getNewBoard(tb, zi):
                    if b not in visited:
                        visited.add(b)
                        queue.append((b,z))

            depth += 1
        
        return -1
