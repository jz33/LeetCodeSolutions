A = ord('a')

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isEnd = False; # if there is a word ends here
        self.children = [None] * 26 # a list of 26 possible children
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        this = self # use this pointer to avoid recursive
        for c in word:
            i = ord(c) - A
            if this.children[i] is None:
                this.children[i] = Trie()
            this = this.children[i]
        this.isEnd = True    

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        this = self # use this pointer to avoid recursive
        for c in word:
            i = ord(c) - A
            if this.children[i] is None:
                return False           
            this = this.children[i]
        return this.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        this = self # use this pointer to avoid recursive
        for c in prefix:
            i = ord(c) - A
            if this.children[i] is None:
                return False           
            this = this.children[i]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
