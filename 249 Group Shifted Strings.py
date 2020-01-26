'''
249. Group Shifted Strings
https://leetcode.com/problems/group-shifted-strings/

Given a string, we can "shift" each of its letter to its successive letter,
for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets,
group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
'''
class Solution:
    def getHash(self, s: str) -> str:
        if not s:
            return ''
        
        A = ord('a')
        
        diff = ord(s[0]) - A
        res = []
        for e in s:
            d = ord(e) - A - diff
            if d < 0:
                d += 26
            res.append(chr(d + A))
            
        return ''.join(res)
        
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        book = collections.defaultdict(list)
        for word in strings:
            h = self.getHash(word)
            book[h].append(word)
        
        return list(book.values())
