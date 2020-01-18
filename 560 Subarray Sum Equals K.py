'''
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/
     
Given an array of integers and an integer k,
you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        book = collections.Counter() # {prefix sum : count}
        book[0] = 1
        preSum = 0 # prefix sum
        for e in nums:
            preSum += e
            res += book[preSum - k]
            book[preSum] += 1
        return res
