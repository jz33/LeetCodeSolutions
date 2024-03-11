'''
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window.
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
        self.patternCounter = Counter(pattern)
        self.patternSize = len(pattern)
        self.validCount = 0
        self.charCounts = Counter()
    
    def isMatched(self) -> bool:
        return self.validCount == self.patternSize
    
    def add(self, char: str):
        newCharCount = self.charCounts[char] + 1
        self.charCounts[char] = newCharCount
        if newCharCount <= self.patternCounter[char]:
            self.validCount += 1
    
    def remove(self, char: str):
        newCharCount = self.charCounts[char] - 1
        self.charCounts[char] = newCharCount
        if newCharCount < self.patternCounter[char]:
            self.validCount -= 1
    
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = SlidingWindow(t)
        result = ''
        left = 0
        for right, val in enumerate(s):
            # Extend
            window.add(val)

            while window.isMatched():
                # Result
                if result == '' or right - left + 1 < len(result):
                    result = s[left : right + 1]
                # Shrink
                window.remove(s[left])
                left += 1
        return result