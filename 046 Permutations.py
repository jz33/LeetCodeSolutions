'''
46. Permutations
https://leetcode.com/problems/permutations/

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms, newPerms = [[]], []      
        for e in nums:
            for row in perms:
                # The idea is to insert e onto all positions
                # of previous permutation
                for i in range(len(row) + 1):
                    newPerms.append(row[:i] + [e] + row[i:])
            perms, newPerms = newPerms, []
        return perms
