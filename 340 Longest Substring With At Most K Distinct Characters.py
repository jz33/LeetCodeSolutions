'''
340. Longest Substring with At Most K Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.

Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
'''
from collections import Counter

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
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
