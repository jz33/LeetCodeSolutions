'''
524. Longest Word in Dictionary through Deleting
https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

Given a string and a string dictionary, find the longest string in the dictionary that
can be formed by deleting some characters of the given string.
If there are more than one possible results, return the longest word with the smallest lexicographical order.
If there is no possible result, return the empty string.

Example 1:

Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:

Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
'''
class Solution:
    def isSubsequence(self, haystack: str, needle: str) -> bool:
        ni = 0
        for h in haystack:
            if h == needle[ni]:
                ni += 1
            if ni == len(needle):
                return True
        return False
        
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = ''
        for w in d:
            if len(w) >= len(res) and self.isSubsequence(s, w):
                if len(w) > len(res):
                    res = w
                elif w < res:
                    res = w       
        return res
