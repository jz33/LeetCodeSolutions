'''
345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"

Example 2:

Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".
'''
class Solution:
    def isVowel(self, s: str) -> bool:
        return s.lower() in ['a','e','i','o','u']
    
    def reverseVowels(self, s: str) -> str:
        ls = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            vi = self.isVowel(s[i])
            vj = self.isVowel(s[j])
            
            if vi and vj:
                ls[i],ls[j] = ls[j],ls[i]
                i += 1
                j -= 1
            elif vi:
                j -= 1
            elif vj:
                i += 1
            else:
                i += 1
                j -= 1
                
        return ''.join(ls)
