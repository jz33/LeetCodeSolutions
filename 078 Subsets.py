'''
78. Subsets
https://leetcode.com/problems/subsets/

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        width = len(nums)
        total = 1 << width
        res = []
        for i in range(total):
            ls = []
            for j in range(width):
                d = (1 << j)
                if d > i:
                    break # early break
                if (i & d) > 0:
                    ls.append(nums[j])
            res.append(ls)
        return res
