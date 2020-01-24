'''
47. Permutations II
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms, newPerms = [[]], []      
        for e in nums:
            for row in perms:
                
                # This basic idea is to insert e onto all positions
                # of previous permutation
                for i in range(len(row) + 1):
                    newPerms.append(row[:i] + [e] + row[i:])
                    
                    # This is the only added line to handle duplicates
                    if i < len(row) and row[i] == e: break 
                    
            perms, newPerms = newPerms, []
        return perms
