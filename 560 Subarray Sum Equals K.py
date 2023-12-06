'''
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k,
return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
    1 <= nums.length <= 2 * 104
    -1000 <= nums[i] <= 1000
    -107 <= k <= 107
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        seen = {0: 1} # {prefix sum : count}
        prefixSum = 0 # current prefix sum
        for e in nums:
            prefixSum += e
            result += seen.get(prefixSum - k, 0)
            seen[prefixSum] = seen.get(prefixSum, 0) + 1
        return result
