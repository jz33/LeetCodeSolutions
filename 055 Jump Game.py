'''
55. Jump Game
https://leetcode.com/problems/jump-game/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
             
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        currPos = 0
        while True:
            nextPos = currPos + nums[currPos]
            if nextPos >= len(nums) - 1:
                return True
            if nextPos == currPos:
                return False
            
            _, currPos = max((nums[i] + i, i) for i in range(currPos+1, nextPos+1))            
        return True
