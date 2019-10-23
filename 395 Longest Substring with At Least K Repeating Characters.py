'''
395. Longest Substring with At Least K Repeating Characters
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

Find the length of the longest substring T of a given string (consists of lowercase letters only) such that
every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''
from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        '''
        Sliding Window method
        '''
        if k == 1:
            return len(s)

        if len(s) < k:
            return 0
        
        maxSize = 0

        # How many distinct chars in s?
        distinctCharCount = len(Counter(s))

        # Iterate, solve individual question: "Longest substring with
        # exactly @d unique chars and each repeats at least k times
        for d in range(1, distinctCharCount+1):
            left = 0
            book = Counter()
            dc = 0 # distinct char count
            rc = 0 # count of chars whose count is at least k
            
            for i,c in enumerate(s):
                # Add current
                book[c] += 1
                if book[c] == 1:
                    dc += 1
                elif book[c] == k:
                    rc += 1

                # Shrink from left
                while dc > d:
                    lc = s[left]
                    book[lc] -= 1
                    if book[lc] == 0:
                        dc -= 1
                    elif book[lc] == k - 1:
                        rc -= 1
                    left += 1

                if dc == d and rc == d:
                    maxSize = max(maxSize, i - left + 1)
        return maxSize
    
class Solution:
    def longestSubstringRecursive(self, ls: List[str], k: int) -> int:
        '''
        Divide and Conquer solution
        '''
        if k < 2:
            return len(ls)
        if len(ls) < k:
            return 0
        
        # Split ls. Delimiter chars are the chars appear less than k times
        counter = Counter(ls)
        maxLength = 0
        left = 0
        foundLesserChar = False
        for i, e in enumerate(ls):
            if counter[e] < k:
                # Try to go subroutine
                # Only if subroutine ls length is bigger than k (k-1) and maxLength
                if i - left > max(k-1, maxLength):
                    # print(left, i, ls)
                    maxLength = max(maxLength, self.longestSubstringRecursive(ls[left:i], k))
                left = i+1
                foundLesserChar = True
        
        # If all chars are equal or greater than k, return ls itself
        if not foundLesserChar:
            return len(ls)
        
        # Last subroutine
        if len(ls) - left > max(k-1, maxLength):
            # print(left, i, ls)
            maxLength = max(maxLength, self.longestSubstringRecursive(ls[left:], k))
        
        return maxLength
    
    def longestSubstring(self, s: str, k: int) -> int:
        return self.longestSubstringRecursive(list(s), k)
