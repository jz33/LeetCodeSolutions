'''
567. Permutation in String
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        book1 = Counter(s1)
        slidingBook = Counter()
        validCount = 0
        left = 0
        for i,c in enumerate(s2):
            if c not in book1:
                slidingBook = Counter()
                validCount = 0
                left = i+1
            else:
                slidingBook[c] += 1
                validCount += 1
                
                # Shrink
                while slidingBook[c] > book1[c]:
                    lc = s2[left]
                    left += 1
                    slidingBook[lc] -= 1
                    validCount -= 1
                                        
                if validCount == len(s1):
                    return True
            
        return False
