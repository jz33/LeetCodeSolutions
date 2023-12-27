'''
126. Word Ladder
https://leetcode.com/problems/word-ladder/

Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.  
'''
'''
Double-sided BFS
Try to find the shorted solutions
Input sample:
hit
cog
hot dot dog lot log
   hit => start
    |
   hot => entries   \
  /   \
dot    lot           tree                       
|       |
dog    log => exits /
  \   /
   cog => ended
'''
from collections import defaultdict
from collections import deque

class Solution:
    def bfs(self, book, dq, visited, visited_otherside):
        word, level = dq.popleft()
        
        for i in range(self.size):
            genericWord = word[:i] + '*' + word[i+1:]
            realWords = book.get(genericWord, [])
            
            for realWord in realWords:             
                if realWord in visited_otherside:
                    return level + visited_otherside[realWord]
                
                if realWord not in visited:
                    dq.append((realWord, level+1))
                    visited[realWord] = level+1
                    
        return None
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        
        self.size = len(beginWord)
           
        # Pre-process wordList to book {generic word : [real word]}
        # A read word is like "world", then a generic word can be "wo*ld"
        book = defaultdict(list)
        for word in wordList:
            for i in range(self.size):
                genericWord = word[:i] + '*' + word[i+1:]
                book[genericWord].append(word)
                     
        # Double sides BFS
        # Notice the visited words are the words that currently in queue,
        # not the words ready to pop 
        visited_top = {beginWord : 1} # word : level
        # Need queue not stack to do Breadth-First search
        dq_top = deque([(beginWord, 1)])
        visited_bottom = {endWord : 1}
        dq_bottom = deque([(endWord, 1)])
 
        while len(dq_top) > 0 and len(dq_bottom) > 0:            
            level = self.bfs(book, dq_top, visited_top, visited_bottom)
            if level:
                return level
            
            level = self.bfs(book, dq_bottom, visited_bottom, visited_top)
            if level:
                return level
            
        return 0
