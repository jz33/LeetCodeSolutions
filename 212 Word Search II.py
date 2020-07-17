'''
212. Word Search II
https://leetcode.com/problems/word-search-ii/

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
'''
class TrieNode:
    def __init__(self):
        self.word = None; # if there is a word ends here, self.word will not be None
        self.children = {} # a list of 26 possible children

    def add(self, word: str) -> None:
        this = self
        for c in word:
            if c not in this.children:
                this.children[c] = TrieNode()
            this = this.children[c]
        this.word = word
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []
        
        rowCount = len(board)
        colCount = len(board[0])
        
        head = TrieNode()
        for word in words:
            head.add(word)

        pool = [] # result
      
        def backtrack(visited, node, i, j):
            if node.word is not None:
                pool.append(node.word)
                node.word = None # kill this word!

            for x, y in (i,j+1), (i+1,j), (i,j-1),(i-1,j):
                if 0 <= x < rowCount and 0 <= y < colCount and (x,y) not in visited:
                    nextNode = node.children.get(board[x][y])
                    if nextNode:
                        visited.add((x,y))
                        backtrack(visited, nextNode, x, y)
                        visited.remove((x,y))
        
        for i in range(rowCount):
            for j in range(colCount):
                letter = board[i][j]
                nextNode = head.children.get(letter)
                if nextNode:
                    visited = {(i,j)}
                    backtrack(visited, nextNode, i, j)

        return pool
