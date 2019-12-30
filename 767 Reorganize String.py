'''
767. Reorganize String
https://leetcode.com/problems/task-scheduler/

Given a string S, check if the letters can be rearranged so that two characters
that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"

Example 2:

Input: S = "aaab"
Output: ""
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
