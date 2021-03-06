'''
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''
class Slider:
    def __init__(self):
        self.book = collections.Counter()
        self.count = 0
    
    def kValue(self) -> int:
        if not self.book:
            return 0
        
        mc = self.book.most_common(1)[0][1]
        return self.count - mc
    
    def add(self, c):
        self.book[c] += 1
        self.count += 1
    
    def remove(self, c):
        self.book[c] -= 1
        self.count -= 1

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        left = 0
        slider = Slider()
        for i, c in enumerate(s):
            slider.add(c)
            while slider.kValue() > k:
                lc = s[left]
                left += 1
                slider.remove(lc)
            maxLen = max(maxLen, slider.count)
        return maxLen
