/*
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/
     
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
*/
from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ctr = Counter() # sum : count
        ctr[0] = 1 # think [1,1,1], 2
        s = 0
        res = 0
        for n in nums:
            s += n
            # Similar idea to Continuous Subarray Sum question
            # So for every j representing the index on ctr[s-k],
            # if say current index is i, then sum of nums[j+1:i+1]
            # must be k
            res += ctr[s-k]
            ctr[s] += 1
        return res
