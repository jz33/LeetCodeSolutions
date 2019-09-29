'''
Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''
    from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Pre-process t
        t_book = Counter(t)
        t_size = len(t)
        
        # Result
        s_size = len(s)
        minWinSize = s_size + 1
        minWinLeft = -1
        
        # Iteration recorder
        left = 0 # left index of current found
        i = 0 # like "right" index
        book = Counter()
        # How many "valid" chars found
        # "valid" means the cound of chars is smaller than that in t_book
        validCount = 0 
        
        # If s is still under iteration or current found still matches
        # even though s is already iterated over
        while i < s_size or validCount == t_size:           
            if validCount < t_size:
                # Not match yet
                c = s[i]
                i += 1
                book[c] += 1
                if book[c] <= t_book[c]:
                    validCount += 1
            else:
                # Matched.
                # Try update result
                count = i - left
                if count < minWinSize:
                    minWinSize = count
                    minWinLeft = left
                    
                # Try shrink from left
                c = s[left]
                left += 1
                book[c] -= 1
                if book[c] < t_book[c]:
                    validCount -= 1
                    
        return s[minWinLeft:minWinLeft+minWinSize] if minWinLeft != -1 else ''
