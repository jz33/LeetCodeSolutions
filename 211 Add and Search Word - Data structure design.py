'''
211. Add and Search Word - Data structure design
https://leetcode.com/problems/add-and-search-word-data-structure-design/

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or ..
A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
'''
class Node: # Trie Node
    def __init__(self):
        self.isWord = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        this = self.root
        for c in word:
            if c not in this.children:
                this.children[c] = Node()
            this = this.children[c]
        this.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        queue = collections.deque()
        queue.append(self.root)
        for c in word:
            if not queue:
                return False
            
            for _ in range(len(queue)):
                node = queue.popleft()
                if c == '.':
                    for n in node.children.values():
                        queue.append(n)
                else:
                    if c in node.children:
                        queue.append(node.children[c])
        
        return any(node.isWord for node in queue)
