'''
745. Prefix and Suffix Search
https://leetcode.com/problems/prefix-and-suffix-search/

Design a special dictionary that searches the words in it by a prefix and a suffix.

Implement the WordFilter class:

    WordFilter(string[] words) Initializes the object with the words in the dictionary.

    f(string pref, string suff) Returns the index of the word in the dictionary,
    which has the prefix pref and the suffix suff. If there is more than one valid index,
    return the largest of them. If there is no such word in the dictionary, return -1.

Example 1:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]
Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".

Constraints:
    1 <= words.length <= 104
    1 <= words[i].length <= 7
    1 <= pref.length, suff.length <= 7
    words[i], pref and suff consist of lowercase English letters only.
    At most 104 calls will be made to the function f
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.pair = None # (word, weight)
        
class WordFilter:
    def __init__(self, words: List[str]):
        self.forwardRoot = TrieNode()
        self.backwardRoot = TrieNode()
        for i, word in enumerate(words):
            self.__add(word, i, False)
            self.__add(word, i, True)
        
    def __add(self, word: str, weight: int, isReversed: bool):
        this = self.backwardRoot if isReversed else self.forwardRoot
        newWord = word[::-1] if isReversed else word
        for e in newWord:
            if e not in this.children:
                this.children[e] = TrieNode()
            this = this.children[e]
        this.pair = (word, weight)
    
    def __search(self, prefix: str, isReversed: bool):
        this = self.backwardRoot if isReversed else self.forwardRoot
        newPrefix = prefix[::-1] if isReversed else prefix
        
        # 1. Go though the prefix or suffix
        for e in newPrefix:
            if e not in this.children:
                return set()
            this = this.children[e]
        
        # 2. Get all words
        queue = deque([this])
        words = set() # [(word, weight)]
        while queue:
            node = queue.popleft()
            if node.pair:
                words.add(node.pair)
            for child in node.children.values():
                queue.append(child)
        return words

    def f(self, prefix: str, suffix: str) -> int:
        left = self.__search(prefix, False)
        right = self.__search(suffix, True)
        ls = sorted(list(left & right), key = lambda pair : -pair[1])
        return -1 if not ls else ls[0][1]
