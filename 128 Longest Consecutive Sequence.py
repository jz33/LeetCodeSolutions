'''
128 Longest Consecutive Sequence.py
https://oj.leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Hashmap, Array
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        ss = set(nums)
        
        while ss:
            e = ss.pop()
            
            # Expand from e
            ctr = 1
            p = e
            while p-1 in ss:
                ctr += 1
                p -= 1
                ss.remove(p)
            p = e
            while p+1 in ss:
                ctr += 1
                p += 1
                ss.remove(p)
                
            res = max(res, ctr)      
        return res
