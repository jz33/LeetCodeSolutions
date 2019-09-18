'''
Given two words (beginWord and endWord), and a dictionary's word list,
find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

Example 3:
beginWord = "magic"
endWord = "pearl"
wordList = ["flail","halon","lexus","joint","pears","slabs","lorie","lapse","wroth","yalow","swear","cavil","piety","yogis","dhaka","laxer","tatum","provo","truss","tends","deana","dried","hutch","basho","flyby","miler","fries","floes","lingo","wider","scary","marks","perry","igloo","melts","lanny","satan","foamy","perks","denim","plugs","cloak","cyril","women","issue","rocky","marry","trash","merry","topic","hicks","dicky","prado","casio","lapel","diane","serer","paige","parry","elope","balds","dated","copra","earth","marty","slake","balms","daryl","loves","civet","sweat","daley","touch","maria","dacca","muggy","chore","felix","ogled","acids","terse","cults","darla","snubs","boats","recta","cohan","purse","joist","grosz","sheri","steam","manic","luisa","gluts","spits","boxer","abner","cooke","scowl","kenya","hasps","roger","edwin","black","terns","folks","demur","dingo","party","brian","numbs","forgo","gunny","waled","bucks","titan","ruffs","pizza","ravel","poole","suits","stoic","segre","white","lemur","belts","scums","parks","gusts","ozark","umped","heard","lorna","emile","orbit","onset","cruet","amiss","fumed","gelds","italy","rakes","loxed","kilts","mania","tombs","gaped","merge","molar","smith","tangs","misty","wefts","yawns","smile","scuff","width","paris","coded","sodom","shits","benny","pudgy","mayer","peary","curve","tulsa","ramos","thick","dogie","gourd","strop","ahmad","clove","tract","calyx","maris","wants","lipid","pearl","maybe","banjo","south","blend","diana","lanai","waged","shari","magic","duchy","decca","wried","maine","nutty","turns","satyr","holds","finks","twits","peaks","teems","peace","melon","czars","robby","tabby","shove","minty","marta","dregs","lacks","casts","aruba","stall","nurse","jewry","knuth"]

Output:
"magic","manic","mania","maria","maris","marks","parks","perks","peaks","pears","pearl"
"magic","manic","mania","maria","maris","paris","parks","perks","peaks","pears","pearl"
"magic","manic","mania","maria","marta","marty","party","parry","perry","peary","pearl"
"magic","manic","mania","maria","marta","marty","marry","parry","perry","peary","pearl"
"magic","manic","mania","maria","marta","marty","marry","merry","perry","peary","pearl"

Look at last 2 rows, from "marry" to right, there are 2 pathes to root "pearl"!
'''
from collections import defaultdict, deque

class Solution:
    def bfs(self, book, row, visited, visited_otherside, isTopDown):
        '''
        Level order traverse (BFS)
        row: a deque containing words on this level
        visited: {word : [pathes to root]}
        isTopDown: BFS direction
        '''
        # Need a separate container for words of next iteration
        # Cannot just push into row!
        nextRow = deque() 
         
        # Need a separate visited map, cannot just push into visited!
        nextVisited = defaultdict(list)
        solution = []
        
        while row:
            word = row.popleft()
            for i in range(self.size):
                genericWord = word[:i] + '*' + word[i+1:]
                realWords = book.get(genericWord, [])            
                for realWord in realWords:                             
                    if realWord in visited_otherside:
                        # Concluded!
                        for path in visited[word]:
                            for path_otherside in visited_otherside[realWord]:
                                if isTopDown:
                                    solution.append(path + path_otherside)
                                else:
                                    solution.append(path_otherside + path)
                    else:
                        if realWord not in visited:
                            # New word cannot be already in nextVisited, because push into deque can cause duplicate
                            if realWord not in nextVisited:
                                nextRow.append(realWord)
                            
                            # But new word can form a path
                            # This is the reason why nextVisited is needed
                            for path in visited[word]:
                                if isTopDown:
                                    nextVisited[realWord].append(path + [realWord])
                                else:
                                    nextVisited[realWord].append([realWord] + path)
                         
        if not solution:
            visited.update(nextVisited)

        return nextRow, solution
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return []
        
        self.size = len(beginWord)
           
        # Pre-process wordList to book {generic word : [real word]}
        # A read word is like "world", then a generic word can be "wo*ld"
        book = defaultdict(list)
        for word in wordList:
            for i in range(self.size):
                genericWord = word[:i] + '*' + word[i+1:]
                book[genericWord].append(word)
                       
        # { word : [pathes to root]}
        # Notice a word can have multiple path to root!
        visited_top = defaultdict(list)
        visited_top[beginWord] = [[beginWord]]
        row_top = deque([beginWord])
        
        visited_bottom = defaultdict(list)
        visited_bottom[endWord] = [[endWord]]
        row_bottom = deque([endWord])
        
        while row_top and row_bottom:           
            nextRow_top, solution = self.bfs(book, row_top, visited_top, visited_bottom, True)
            if solution:
                return solution
            row_top = nextRow_top
   
            nextRow_bottom, solution = self.bfs(book, row_bottom, visited_bottom, visited_top, False)
            if solution:
                return solution
            row_bottom = nextRow_bottom
 
        return []
