'''
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum window
substring
of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:
    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.
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
        newCharCount = self.counter[char] + 1
        self.counter[char] = newCharCount
        if newCharCount <= self.patternCounter[char]:
            self.validCount += 1
    
    def remove(self, char: str):
        newCharCount = self.counter[char] - 1
        self.counter[char] = newCharCount
        if newCharCount < self.patternCounter[char]:
            self.validCount -= 1
    
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = SlidingWindow(t)
        resultStart = None
        resultSize = len(s) + 1 # Not len(s)
        left = 0
        right = 0
        while left < len(s):
            # Extend
            while right < len(s) and not window.isMatched():
                window.add(s[right])
                right += 1
            # Update result
            if (window.isMatched()):
                size = right - left
                if size < resultSize:
                    resultSize = size
                    resultStart = left
            # Shrink
            window.remove(s[left])
            left += 1

        return s[resultStart : resultStart + resultSize] if resultStart is not None else ''
