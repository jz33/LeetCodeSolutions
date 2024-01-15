'''
79. Word Search
https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board
'''
from collections import Counter
class Solution:
    '''
    This is NOT a BFS problem, because there cannot be a global "visited" cache.
    Think example:
    [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    "ABCESEEEFS"
    '''                   
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Search prune to remove ridiculous cases
        rowCount = len(board)
        colCount = len(board[0])
        if len(word) > rowCount * colCount:
            return False
        
        counterBoard = Counter()
        for i in range(rowCount):
            for j in range(colCount):
                counterBoard[board[i][j]] += 1
        for value, count in Counter(word).items():
            if counterBoard.get(value, 0) < count:
                return False
            
        # DFS
        visited = set()

        def backtrack(wi: int, i: int, j: int) -> bool:
            nonlocal visited
            if wi == len(word):
                return True
            
            for x, y in (i,j+1), (i+1,j), (i,j-1),(i-1,j):
                if 0 <= x < rowCount and 0 <= y < colCount and (x,y) not in visited and board[x][y] == word[wi]:
                    visited.add((x,y))
                    if backtrack(wi+1, x, y):
                        return True
                    visited.remove((x,y))

            return False

        for i in range(rowCount):
            for j in range(colCount):
                if board[i][j] == word[0]:
                    visited = {(i,j)}
                    if backtrack(1, i, j):
                        return True
    
        return False
