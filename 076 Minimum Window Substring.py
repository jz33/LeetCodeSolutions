'''
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''
class SlidingWindow:
    def __init__(self, pattern: str):
        self.patternCounter = collections.Counter(pattern)
        self.patternSize = len(pattern)
        self.validCount = 0
        self.counter = collections.Counter()
    
    def isMatched(self) -> bool:
        return self.validCount == self.patternSize
    
    def add(self, char: str):
        self.counter[char] += 1
        if self.counter[char] <= self.patternCounter[char]:
            self.validCount += 1
    
    def remove(self, char: str):
        self.counter[char] -= 1
        if self.counter[char] < self.patternCounter[char]:
            self.validCount -= 1
    
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sw = SlidingWindow(t)
        resultStart = None
        resultSize = len(s) + 1 # Not len(s)
        i = 0
        start = 0
        while i < len(s) or sw.isMatched():        
            if not sw.isMatched():
                # Not match yet
                c = s[i]
                i += 1
                sw.add(c)
            else:
                # Matched.
                # Try update result
                size = i - start
                if size < resultSize:
                    resultSize = size
                    resultStart = start

                # Shrink from left
                c = s[start]
                start += 1
                sw.remove(c)
    
        return s[resultStart : resultStart + resultSize] if resultStart is not None else ''
