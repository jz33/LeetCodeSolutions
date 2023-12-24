'''
676. Implement Magic Dictionary
https://leetcode.com/problems/implement-magic-dictionary/description/

Design a data structure that is initialized with a list of different words.
Provided a string, you should determine if you can change exactly one character in
this string to match any word in the data structure.

Implement the MagicDictionary class:

MagicDictionary() Initializes the object.

void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.

bool search(String searchWord) Returns true if you can change exactly one character in
searchWord to match any string in the data structure, otherwise returns false.

Example 1:

Input
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
Output
[null, null, false, true, false, false]

Explanation
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // return False
magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match "hello" so we return True
magicDictionary.search("hell"); // return False
magicDictionary.search("leetcoded"); // return False

Constraints:
    1 <= dictionary.length <= 100
    1 <= dictionary[i].length <= 100
    dictionary[i] consists of only lower-case English letters.
    All the strings in dictionary are distinct.
    1 <= searchWord.length <= 100
    searchWord consists of only lower-case English letters.
    buildDict will be called only once before search.
    At most 100 calls will be made to search.
'''
class Trie:
    def __init__(self):
        self.oriWord = None
        self.children = [None] * 26
        
    def insert(self, word: str) -> None:
        this = self
        for c in word:
            i = ord(c) - ord('a')
            if this.children[i] is None:
                this.children[i] = Trie()
            this = this.children[i]
        this.oriWord = word    

class MagicDictionary:
    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)

    def search(self, word: str) -> bool:

        def dfs(wordIndex: int, misMatch: int, node: Trie) -> bool:
            if misMatch > 1:
                return False
            if wordIndex == len(word):
                return node.oriWord is not None and misMatch == 1
            
            i = ord(word[wordIndex]) - ord('a')
            for ci in range(26):
                if node.children[ci] is not None:
                    if ci == i and dfs(wordIndex + 1, misMatch, node.children[ci]):
                        return True
                    if ci != i and dfs(wordIndex + 1, misMatch + 1, node.children[ci]):
                        return True
            return False

        return dfs(0, 0, self.trie)