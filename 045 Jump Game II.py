'''
45. Jump Game II
https://leetcode.com/problems/jump-game-ii/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2

Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        currPos = 0
        for steps in range(1, len(nums)):
            nextPos = currPos + nums[currPos]
            
            if nextPos >= len(nums) - 1:
                return steps
            
            if nextPos == currPos:
                return -1
            
            _, currPos = max((nums[i] + i, i) for i in range(currPos+1, nextPos+1))
            
        return -1
