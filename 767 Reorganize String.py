'''
767. Reorganize String
https://leetcode.com/problems/reorganize-string/

Given a string s, rearrange the characters of s so that
any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Example 1:

Input: s = "aab"
Output: "aba"

Example 2:

Input: s = "aaab"
Output: ""

Constraints:
    1 <= s.length <= 500
    s consists of lowercase English letters.
'''
class Solution:
    def reorganizeString(self, S: str) -> str:
        '''
        Same idea to 621. Task Scheduler
        '''
        # 1. Get the most common char
        ctr = collections.Counter(S)      
        topChar, topCharCount = ctr.most_common(1)[0]
        
        # We separate top chars, set each top task with 1 empty slot to each other.
        # If rest of chars cannot fill the slots, not possible
        if len(S) - topCharCount < topCharCount - 1:
            return ''
        
        # 2. Build buckets of chars, first char of each bucket is the top char.
        # Fill other chars to buckets
        buckets = [[topChar] for _ in range(topCharCount)]
        bi = 0
        for char, count in ctr.items():
            if char != topChar:
                for _ in range(count):
                    buckets[bi].append(char)
                    bi += 1
                    if bi == len(buckets):
                        bi = 0       
        return ''.join(''.join(b) for b in buckets)        
