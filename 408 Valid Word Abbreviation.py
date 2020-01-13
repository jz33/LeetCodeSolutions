'''
408. Valid Word Abbreviation
https://leetcode.com/problems/valid-word-abbreviation/

Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

Notice that only the above abbreviations are valid abbreviations of the string "word".
Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:

Given s = "internationalization", abbr = "i12iz4n":

Return true.

Example 2:

Given s = "apple", abbr = "a2e":

Return false.
'''
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0 # index of word
        num = 0
        for a in abbr:
            if a.isalpha():
                if num > 0:
                    i += num
                    num = 0
                
                if i >= len(word) or word[i] != a:
                    return False              
                i += 1
                
            else:
                if num == 0 and a == '0':
                    return False
                num = num * 10 + int(a)
                
        if num > 0:
            i += num
        
        return i == len(word)
