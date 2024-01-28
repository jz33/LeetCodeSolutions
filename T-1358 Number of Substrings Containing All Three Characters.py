'''
1358. Number of Substrings Containing All Three Characters
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c
are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:

Input: s = "abc"
Output: 1

Constraints:
    3 <= s.length <= 5 x 10^4
    s only consists of a, b or c characters.
'''
from collections import Counter

class Window:
    def __init__(self):
        self.counter = Counter([('a', 0), ('b', 0), ('c', 0)])

    def isValid(self) -> bool:
        return self.counter['a'] > 0 and self.counter['b'] > 0 and self.counter['c'] > 0
    
    def add(self, c: str):
        self.counter[c] += 1

    def remove(self, c: str):
        self.counter[c] -= 1

class Solution:
    '''
    A standard sliding window solution
    '''
    def numberOfSubstrings(self, src: str) -> int:
        result = 0
        window = Window()
        left, right = 0, 0
        while left < len(src):
            # Extend
            while right < len(src) and not window.isValid():   
                char = src[right]
                window.add(char)
                right += 1

            # Result
            if window.isValid():
                # If a substring [left: right] is valid,
                # all substrings of [left:right], [left: right+1],... are valid
                # Notice here right is 1 index out of last valid substring
                result += len(src) - right + 1
            
            # Shrink
            leftChar = src[left]
            window.remove(leftChar)
            left += 1
        return result

class Solution:
    '''
    Simpler hashmap solution
    '''
    def numberOfSubstrings(self, src: str) -> int:
        result = 0
        # The seen records the seen last index of 'a' or 'b' or 'c'.
        # It is an array so it's easy to get min
        # If a char is -1 it means it is not seen yet
        seen = [-1] * 3
        for i, c in enumerate(src):
            seen[ord(c) - ord('a')] = i
            # If substring [a : b] is valid, all substrings [a-1:b]...[0:b] are valid
            # Then, get the 1st appearance of the valid substring, which is min(seen)
            # If there is an char not yet appear, min(seen) will be -1
            result += 1 + min(seen)
        return result