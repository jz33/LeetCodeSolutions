'''
792. Number of Matching Subsequences
https://leetcode.com/problems/number-of-matching-subsequences/

Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
'''
from collections import defaultdict, deque

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        # Build {starting char : deque(word)} dictionary
        book = defaultdict(deque)
        for word in words:
            book[word[0]].append(list(word))
        
        # Iterate S, if a char of S is starting char of a word,
        # "move" this word forward
        res = 0
        for c in S:
            queue = book[c]
            for _ in range(len(queue)):
                word = queue.popleft()
                if len(word) == 1:
                    res += 1
                else:
                    word = word[1:]
                    book[word[0]].append(word)
                    
        return res          
