'''
90. Subsets II
https://leetcode.com/problems/subsets-ii/

Given a collection of integers that might contain duplicates,
nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''
from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        dp = [[]]
        for key, count in counter.items():
            newDp = []
            for times in range(count+1):
                added = [key] * times
                for comb in dp:
                    newDp.append(comb + added)
            dp = newDp
        return dp
