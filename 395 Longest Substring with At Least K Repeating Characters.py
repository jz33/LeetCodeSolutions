'''
395. Longest Substring with At Least K Repeating Characters
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

Given a string s and an integer k, return the length of the longest substring of s such that
the frequency of each character in this substring is greater than or equal to k.

if no such substring exists, return 0.

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

Constraints:
    1 <= s.length <= 104
    s consists of only lowercase English letters.
    1 <= k <= 105
'''
from collections import Counter

class Solution:
    def longestSubstring(self, src: str, repeat: int) -> int:
        if repeat == 1:
            return len(src)

        if len(src) < repeat:
            return 0
        
        maxSize = 0

        # How many distinct chars in s?
        distinctCharCount = len(Counter(src))

        # Iterate, solve individual question: "Longest substring with
        # exactly @d unique chars and each repeats at least k times
        for d in range(1, distinctCharCount+1):
            left = 0
            book = Counter() # {char : appearance count}
            distinctCount = 0 # distinct char count
            repeatCount = 0 # count of chars whose count is at least k
            
            for i, c in enumerate(src):
                # Add current
                book[c] += 1
                if book[c] == 1:
                    distinctCount += 1
                elif book[c] == repeat:
                    repeatCount += 1

                # Shrink from left
                while distinctCount > d:
                    lc = src[left]
                    book[lc] -= 1
                    if book[lc] == 0:
                        distinctCount -= 1
                    elif book[lc] == repeat - 1:
                        repeatCount -= 1
                    left += 1

                if distinctCount == d and repeatCount == d:
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
