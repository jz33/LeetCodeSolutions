'''
1032. Stream of Characters
https://leetcode.com/problems/stream-of-characters/

Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried
(in order from oldest to newest, including this letter just queried) spell one of the words in the given list.

Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class StreamChecker:
    def add(self, word: str):
        this = self.root
        # Use 'reversed' to avoid string copy
        for e in reversed(word):
            if e not in this.children:
                this.children[e] = TrieNode()
            this = this.children[e]
        this.isEnd = True
    
    def search(self) -> bool:
        this = self.root
        for e in reversed(self.stream):
            if this.isEnd:
                return True
            if e not in this.children:
                return False
            this = this.children[e]
        return this.isEnd
        
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            self.add(word)
        self.stream = []

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        return self.search()
