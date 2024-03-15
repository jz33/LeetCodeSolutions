'''
45. Jump Game II
https://leetcode.com/problems/jump-game-ii/

You are given a 0-indexed array of integers nums of length n.
You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i.
In other words, if you are at nums[i], you can jump to any nums[i + j] where:

    0 <= j <= nums[i] and
    i + j < n

Return the minimum number of jumps to reach nums[n - 1].
The test cases are generated such that you can reach nums[n - 1].

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
    1 <= nums.length <= 104
    0 <= nums[i] <= 1000
    It's guaranteed that you can reach nums[n - 1]
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest = 0 # farthest position can reach
        curr = 0 # current position
        for i, n in enumerate(nums):
            if curr >= len(nums) - 1:
                break
            farthest = max(farthest, i + n)
            if i == curr:
                # jump to farthest
                curr = farthest
                jumps += 1
        return jumps