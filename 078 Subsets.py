'''
78. Subsets
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for mask in range(1 << len(nums)):
            # Check each bit of t, if is '1', then select nums[i]
            row = []
            for ni in range(len(nums)):
                checker = 1 << ni
                if checker > mask:
                    # If checker > t, no more '1's on left
                    break
                if checker & mask:
                    row.append(nums[ni])
            result.append(row)
        return result
