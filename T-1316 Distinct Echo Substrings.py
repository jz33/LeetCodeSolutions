'''
1316. Distinct Echo Substrings
https://leetcode.com/problems/distinct-echo-substrings/

Return the number of distinct non-empty substrings of text that can be written as
the concatenation of some string with itself (i.e. it can be written as a + a where a is some string).

Example 1:

Input: text = "abcabcabc"
Output: 3
Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".

Example 2:

Input: text = "leetcodeleetcode"
Output: 2
Explanation: The 2 substrings are "ee" and "leetcodeleetcode".
 
Constraints:

1 <= text.length <= 2000
text has only lowercase English letters.
'''
class Solution:
    def isCycled(self, s: str) -> bool:
        half = len(s) // 2
        return s[:half] == s[half:]
    
    def distinctEchoSubstrings(self, text: str) -> int:
        ctr = 0
        visited = set()
        for i in range(2, len(text)+1):
            start = i % 2
            for j in range(start, i-1, 2):
                sub = text[j:i]
                if sub not in visited:
                    if self.isCycled(sub):
                        ctr += 1
                    visited.add(sub)
        return ctr
