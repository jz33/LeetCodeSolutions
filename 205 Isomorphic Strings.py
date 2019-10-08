'''
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapper = {} # map char in s to char in t
        used = set() # check if char in t is used
        
        for i in range(len(s)):
            cs = s[i]
            ct = t[i]
            if cs in mapper:
                if mapper[cs] != ct:
                    # cs is pointed to another char, wrong
                    return False
            else:
                if ct in used:
                    # ct is already pointed to another char
                    return False
            
                mapper[cs] = ct
                used.add(ct)
                
        return True
