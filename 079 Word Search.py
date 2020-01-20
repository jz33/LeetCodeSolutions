'''
79. Word Search
https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''
class Solution:
    def backtrack(self, visited, wi, node) -> bool:
        if wi == len(self.word):
            return True
        
        rowCount = len(self.board)
        colCount = len(self.board[0])
        
        i,j = node
        for x, y in (i,j+1), (i+1,j), (i,j-1),(i-1,j):
            if 0 <= x < rowCount and 0 <= y < colCount and (x,y) not in visited and self.board[x][y] == self.word[wi]:
                visited.add((x,y))
                if self.backtrack(visited, wi+1, (x,y)):
                    return True
                visited.remove((x,y))
        return False
                        
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        
        if not board or not board[0] or len(word) > len(board) * len(board[0]):
            return False
        
        # This is NOT a BFS problem, because there cannot be a global "visited" cache.
        # Think example:
        # [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
        # "ABCESEEEFS"
        
        self.board = board
        self.word = word
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = {(i,j)}
                    if self.backtrack(visited, 1, (i,j)):
                        return True
        return False
