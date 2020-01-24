'''
46. Permutations
https://leetcode.com/problems/permutations/

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms, newPerms = [[]], []      
        for e in nums:
            for row in perms:
                
                # This basic idea is to insert e onto all positions
                # of previous permutation
                for i in range(len(row) + 1):
                    newPerms.append(row[:i] + [e] + row[i:])
                    
            perms, newPerms = newPerms, []
        return perms
