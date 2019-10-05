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
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p or len(s) < len(p):
            return []
        
        p_book = Counter(p)
        p_size = len(p)
        
        # Iteration recorder (the sliding window)
        book = Counter()
        validCount  = 0 # found valid chars
        
        res = []
        for i, c in enumerate(s):
            # Remove old char
            if i - p_size > -1:
                old_char = s[i-p_size]
                book[old_char] -= 1
                if book[old_char] < p_book[old_char]:
                    validCount -= 1
            
            # Add new char
            book[c] += 1
            if book[c] <= p_book[c]:
                validCount += 1
                         
            # Update Result
            if validCount == p_size:
                res.append(i - p_size + 1)
                
        return res
