'''
159. Longest Substring with At Most Two Distinct Characters

Given a string s , find the length of the longest substring t that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.

Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
'''
from collections import Counter

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # Same method as in 340. Longest Substring with At Most K Distinct Characters
        k = 2
        
        if len(s) <= k:
            return len(s)
        
        # Result
        maxSize = k
        
        # Sliding window caches
        left = 0
        book = Counter()
        distinctCount = 0
        
        for i, c in enumerate(s):
            book[c] += 1
            if book[c] == 1:
                distinctCount += 1
                
            # Shrink
            while distinctCount > k:
                lc = s[left]
                book[lc] -= 1
                if book[lc] == 0:
                    distinctCount -= 1
                left += 1
   
            maxSize = max(maxSize, i - left + 1)
                    
        return maxSize
