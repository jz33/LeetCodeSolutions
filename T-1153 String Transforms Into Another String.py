'''
1153. String Transforms Into Another String
https://leetcode.com/problems/string-transforms-into-another-string/

Given two strings str1 and str2 of the same length,
determine whether you can transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.

Example 1:

Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
Example 2:

Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.
'''
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        '''
        A char in str1 can only point to 1 char in str2,
        however, multiple chars in str1 can point to same char in str2
        '''
        book = {}
        for i in range(len(str1)):
            if str1[i] not in book:
                book[str1[i]] = str2[i]
                
            elif book[str1[i]] != str2[i]:
                return False
        
        '''
        Notice the conversion can be:
        aabb => ffbb => ffcc => cccc
        So if a char ('a') in str1 points to a char ('c') in str2 that is also
        appeared in str1, this char ('a') can be converted to a spare char ('f')
        first and then convert later. So if there is a spare char this conversion 
        will work, or str1 and str2 have to be identical
        '''
        return str1 == str2 or len(set(str2)) < 26
