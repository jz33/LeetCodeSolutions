'''
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
class SlidingWindow:
    def __init__(self, pattern: str):
        self.pattern = pattern
        self.histo = Counter(pattern)
        self.validCount = 0
        self.seen = collections.Counter()
        
    def remove(self, char: str):
        self.seen[char] -= 1
        if self.seen[char] < self.histo[char]:
            self.validCount -= 1
            
    def add(self, char: str):
        self.seen[char] += 1
        if self.seen[char] <= self.histo[char]:
            self.validCount += 1

    def isValid(self) -> bool:
        return self.validCount == len(self.pattern)
    
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p or len(s) < len(p):
            return []
        
        sw = SlidingWindow(p)
        
        res = []
        for i, c in enumerate(s):
            # Remove old char
            if i >= len(p):
                char = s[i - len(p)]
                sw.remove(char)

            # Add new char
            sw.add(c)
      
            # Update Result
            if sw.isValid():
                res.append(i - len(p) + 1)
                
        return res
