'''
642. Design Search Autocomplete System
https://leetcode.com/problems/design-search-autocomplete-system/

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.

 
Example:
Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
The system have already tracked down the following sentences and their corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love leetcode" : 2 times
Now, the user begins another search:

Operation: input('i')
Output: ["i love you", "island","i love leetcode"]
Explanation:
There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

Operation: input(' ')
Output: ["i love you","i love leetcode"]
Explanation:
There are only two sentences that have prefix "i ".

Operation: input('a')
Output: []
Explanation:
There are no sentences that have prefix "i a".

Operation: input('#')
Output: []
Explanation:
The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.

 
Note:

The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
Please use double-quote instead of single-quote when you write test cases even for a character input.
Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.
'''
from collections import deque
from heapq import heappush, heappop

class TrieNode:
    def __init__(self):
        # The frequency of the sentence. 0 means not a sentence ends here
        self.frequency = 0
        # [a-z], last slot is space
        self.children = [None] * 27
        self.sentence = None

    def __lt__(self, that):
        if self.frequency != that.frequency:
            return self.frequency < that.frequency
        else:
            return self.sentence > that.sentence

class TrieCollection:
    def __init__(self):
        self.root = TrieNode()
        
    def getIndex(self, c: str) -> int:
        '''
        Get index of given char
        '''
        if c == ' ':
            return 26
        else:
            return ord(c) - ord('a')

    def insert(self, sentence: str, frequency = None):
        this = self.root # use this pointer to avoid recursive
        for c in sentence:
            i = self.getIndex(c)
            if this.children[i] is None:
                this.children[i] = TrieNode()
            this = this.children[i]
        
        this.sentence = sentence
        if frequency:
            this.frequency = frequency
        else:
            this.frequency += 1
    
    def top3(self, prefix: List[str]) -> List[str]:
        # 1. Navigate to the starting node
        this = self.root # use this pointer to avoid recursive
        for c in prefix:
            i = self.getIndex(c)
            if this.children[i] is None:
                return []         
            this = this.children[i]
        
        # 2. Return top 3 frequency sentences under 'this'
        heap = [] # min heap, top 1 is least frequent
        queue = deque([this])
        while queue:
            node = queue.popleft()
            if node.frequency > 0:
                heappush(heap, node)
                if len(heap) > 3:
                    heappop(heap)

            for child in node.children:
                if child:
                    queue.append(child)
    
        arr = []
        while heap:
            node = heappop(heap)
            arr.append(node.sentence)
        arr.reverse()
        return arr
            
class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        trie = TrieCollection()
        for i in range(len(sentences)):
            sentence = sentences[i]
            frequency = times[i]
            trie.insert(sentence, frequency)

        self.trie = trie
        self.prefix = [] # list of input chars

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.trie.insert(''.join(self.prefix))
            self.prefix = []
            return []
        else:
            self.prefix.append(c)
            return self.trie.top3(self.prefix)
