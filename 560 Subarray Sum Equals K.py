"""
560 Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k
"""
def subarraySum(nums, k):
      """
      :type nums: List[int]
      :type k: int
      :rtype: int
      Same method like 523 Continous Subarray Sum
      """
      ref = {0:1} # total : how many total
      total = 0
      counter = 0
      for i,c in enumerate(nums):
          total += c
          counter += ref.get(total-k, 0)
          ref[total] = ref.get(total,0)+1
      return counter
