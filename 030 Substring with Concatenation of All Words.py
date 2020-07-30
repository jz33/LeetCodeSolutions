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
class SlidingWindow:
    def __init__(self, refer, referCount):
        self.refer = refer
        self.referCount = referCount
        self.reset()
        
    def reset(self):
        self.win = collections.Counter()
        self.winCount = 0
        
    def isMatched(self) -> bool:
        return self.winCount == self.referCount

    def add(self, e: str):
        self.win[e] += 1
        if self.win[e] <= self.refer[e]:
            self.winCount += 1
    
    def pop(self, e: str):
        self.win[e] -= 1
        if self.win[e] < self.refer[e]:
            self.winCount -= 1
    
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
    
        width = len(words[0])
        if width * len(words) > len(s):
            return []
        
        refer = collections.Counter(words)
        result = []
        
        # Performing sliding window matching on each width
        for start in range(width):
            sw = SlidingWindow(refer, len(words))
            left = start
            for right in range(start, len(s), width):
                substr = s[right : right + width]
                
                if substr not in refer:
                    sw.reset()
                    left = right + width
                else:         
                    sw.add(substr)
                    
                    if right - left == width * len(words):
                        leftSubstr = s[left : left + width]
                        left += width
                        sw.pop(leftSubstr)
                
                    if sw.isMatched():
                        result.append(left)
                        
        return result
