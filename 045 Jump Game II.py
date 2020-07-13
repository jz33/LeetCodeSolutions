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
        
        jump = 0 # current position ready to jump
        steps = 1
        while nums[jump] != 0: # if cannot jump anywhere, bail
          
            # Get right bound of this jump
            right = jump + nums[jump]
            if right >= len(nums) - 1:
                return steps
            
            # Determine where to jump next
            # Be greedy, choose next position who has max jump for next round
            maxJump = 0
            for i in range(jump + 1, right + 1):
                nexJump = i + nums[i]
                if nexJump >= maxJump: # >= is better than >
                    maxJump = nexJump
                    jump = i
            
            steps += 1

        return -1
