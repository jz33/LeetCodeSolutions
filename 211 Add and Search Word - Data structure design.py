SIZE = 26
A = ord('a')

class TrieNode(object):   
    def __init__(self):
        self.ended = False
        self.sub = [None] * SIZE
    
    def insert(self, word, offset):
        if offset == len(word):
            self.ended = True
        elif offset < len(word):
            i = ord(word[offset]) - A;
            if self.sub[i] is None:
                self.sub[i] = TrieNode()
            self.sub[i].insert(word,offset+1)

    def exists(self, word, offset):
        if offset == len(word):
            return self.ended
        elif offset < len(word):
            c = word[offset]
            if c == '.':
                for i in xrange(0,SIZE):
                    if self.sub[i] is not None and self.sub[i].exists(word,offset+1):
                        return True
                return False
            else:
                i = ord(c) - A
                return self.sub[i] is not None and self.sub[i].exists(word,offset+1)
                
class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.node = TrieNode()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        self.node.insert(word,0)

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.node.exists(word,0)
