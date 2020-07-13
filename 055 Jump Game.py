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
        if len(nums) < 2:
            return True
        
        jump = 0 # current position ready to jump
        while nums[jump] != 0: # if cannot jump anywhere, bail
          
            # Get right bound of this jump
            right = jump + nums[jump]
            if right >= len(nums) - 1:
                return True
            
            # Determine where to jump next
            # Be greedy, choose next position who has max jump for next round
            maxJump = 0
            for i in range(jump + 1, right + 1):
                nexJump = i + nums[i]
                if nexJump >= maxJump:
                    maxJump = nexJump
                    jump = i

        return False
