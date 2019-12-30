'''
213. House Robber II
https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
'''
class Solution:
    def getMaxCash(self, nums: List[int], dp: List[int]) -> int:
        for i in range(2, len(nums)):
            di = i % 3
            dp[di] = max(dp[di-1], dp[di-2] + nums[i])
        return dp[(len(nums) - 1) % 3]
        
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
 
        # Rob 1st house, not 2nd house, not last house
        dp0 = [nums[0], nums[0], None]
        # Rob 2nd house, not 1st house, potentially last house
        dp1 = [0, nums[1], None]

        return max(self.getMaxCash(nums[:-1], dp0), self.getMaxCash(nums, dp1))
