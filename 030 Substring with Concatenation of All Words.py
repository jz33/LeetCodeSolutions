'''
30. Substring with Concatenation of All Words
https://leetcode.com/problems/substring-with-concatenation-of-all-words/

You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and
without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
'''
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        width = len(words[0])
        if width * len(words) > len(s):
            return []
        
        wordsBook = Counter(words) # {word : count}
        res = []
        
        for i in range(width):          
            # Do sliding window
            sBook = Counter()
            found = 0
            left = i
            for j in range(i, len(s), width):
                substr = s[j : j + width]
                if substr in wordsBook:
                    # Shrink
                    while sBook[substr] == wordsBook[substr]:
                        leftSubstr = s[left: left + width]
                        left += width
                        sBook[leftSubstr] -= 1
                        found -= 1
                    
                    # Extend
                    sBook[substr] += 1
                    found += 1
                    
                    # Update result
                    if found == len(words):
                        res.append(left)
                else:
                    # Reset
                    sBook = Counter()
                    found = 0
                    left = j + width
        
        return res
