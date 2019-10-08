'''
358. Rearrange String k Distance Apart
https://leetcode.com/problems/rearrange-string-k-distance-apart/

Given a non-empty string s and an integer k,
rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters.
If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc" 
Explanation: The same letters are at least distance 3 from each other.

Example 2:

Input: s = "aaabc", k = 3
Output: "" 
Explanation: It is not possible to rearrange the string.

Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.
'''
from collections import Counter
from heapq import heappush, heappop

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        '''
        The idea is, schedule top most task in first spot of each cycle k,
        other spot fills in the current most common task 
        '''
        if k == 0:
            return s
        
        histo = Counter(s)
        
        # Set aside top task
        top = histo.most_common(1)
        topTask = top[0][0]
        topCount = top[0][1]

        # A max heap keeps all tasks except top task
        heap = [] # [(count, task)], max heap
        for task, count in histo.items():
            if task != topTask:
                heappush(heap, (-count,task))

        res = [None] * len(s)
        popOuts = []
        for i in range(len(s)):
            t = i % k
            if t == 0 and topCount > 0:
                # If top task available, use it
                res[i] = topTask
                topCount -= 1
            else:
                if len(heap) == 0:
                    return ''

                # Otherwise use the most common one
                mostCommon = heappop(heap)
                task = mostCommon[1]       
                res[i] = task

                count = -mostCommon[0]
                count -= 1
                if count > 0:
                    popOuts.append((-count, task))

            # Put back the entries after a cycle
            if t == k - 1:
                while popOuts:
                    heappush(heap, popOuts.pop())

        return ''.join(res)
