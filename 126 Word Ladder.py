'''
126. Word Ladder
https://leetcode.com/problems/word-ladder/

A transformation sequence from word beginWord to word endWord using a dictionary wordList is
a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.

Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.

sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList,
return the number of words in the shortest transformation sequence from beginWord to endWord,
or 0 if no such sequence exists.

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Constraints:
    1 <= beginWord.length <= 10
    endWord.length == beginWord.length
    1 <= wordList.length <= 5000
    wordList[i].length == beginWord.length
    beginWord, endWord, and wordList[i] consist of lowercase English letters.
    beginWord != endWord
    All the words in wordList are unique.
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
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        
        wordWidth = len(beginWord)
           
        # Pre-process wordList to book {generic word : [real word]}
        # A read word is like "world", then a generic word can be "wo*ld"
        book = collections.defaultdict(list)
        for word in wordList:
            for i in range(wordWidth):
                genericWord = word[:i] + '*' + word[i+1:]
                book[genericWord].append(word)

        def bfs(queue: List[str], visited: Set[str], visitedOther: Set[str]):
            newQueue = []
            for word in queue:
                for i in range(wordWidth):
                    genericWord = word[:i] + '*' + word[i+1:]                
                    for realWord in book.get(genericWord, []):             
                        if realWord in visitedOther:
                            return True, newQueue
                        
                        if realWord not in visited:
                            visited.add(realWord)
                            newQueue.append(realWord)
            return False, newQueue
                     
        # Double sided breadth first search
        visitedTop = { beginWord }
        visitedBottom = { endWord }
        queueTop = [beginWord]
        queueBottom = [endWord]
 
        level = 2
        while queueTop and queueBottom:            
            found, queueTop = bfs(queueTop, visitedTop, visitedBottom)
            if found:
                return level
            level += 1
            
            found, queueBottom = bfs(queueBottom, visitedBottom, visitedTop)
            if found:
                return level
            level += 1
        return 0