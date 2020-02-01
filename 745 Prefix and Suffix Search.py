'''
745. Prefix and Suffix Search
https://leetcode.com/problems/prefix-and-suffix-search/

Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix).
It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

Examples:

Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1
 
Note:

words has length in range [1, 15000].
For each test case, up to words.length queries WordFilter.f may be made.
words[i] has length in range [1, 10].
prefix, suffix have lengths in range [0, 10].
words[i] and prefix, suffix queries consist of lowercase letters only.
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.pair = None # (word, weight)
        
class WordFilter:
    def __init__(self, words: List[str]):
        self.forwardRoot = TrieNode()
        self.backwardRoot = TrieNode()
        
        size = len(words)
        for i, word in enumerate(words):
            self.add(word, i, False)
            self.add(word, i, True)
        
    def add(self, word: str, weight: int, isReversed: bool):
        this = self.backwardRoot if isReversed else self.forwardRoot
        newWord = word[::-1] if isReversed else word
        for e in newWord:
            if e not in this.children:
                this.children[e] = TrieNode()
            this = this.children[e]
        this.pair = (word, weight)
    
    def search(self, prefix: str, isReversed: bool):
        this = self.backwardRoot if isReversed else self.forwardRoot
        newPrefix = prefix[::-1] if isReversed else prefix
        
        # 1. Go though the prefix or suffix
        for e in newPrefix:
            if e not in this.children:
                return set()
            this = this.children[e]
        
        # 2. Get all words
        queue = collections.deque([this])
        words = set() # [(word, weight)]
        while queue:
            node = queue.popleft()
            if node.pair:
                words.add(node.pair)
            for key, child in node.children.items():
                queue.append(child)
        return words

    def f(self, prefix: str, suffix: str) -> int:
        left = self.search(prefix, False)
        right = self.search(suffix, True)
        ls = sorted(list(left & right), key = lambda pair : -pair[1])
        return -1 if not ls else ls[0][1]
