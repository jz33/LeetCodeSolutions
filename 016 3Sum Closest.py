'''
16. 3Sum Closest
https://leetcode.com/problems/3sum-closest

Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

Constraints:
    3 <= nums.length <= 500
    -1000 <= nums[i] <= 1000
    -104 <= target <= 104
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = None
        start = 0
        while start < len(nums) - 2:
            startVal = nums[start]
            left = start + 1
            right = len(nums) - 1
            while left < right:
                leftVal = nums[left]
                rightVal = nums[right]
                total = leftVal + rightVal + startVal
                if total == target:
                    return target
                if closest is None or abs(total - target) < abs(closest - target):
                    closest = total
                if total < target:
                    left += 1
                    while left < right and nums[left] == leftVal:
                        left += 1
                if total > target:
                    right -= 1
                    while left < right and nums[right] == rightVal:
                        right -= 1
            start += 1
            while start < len(nums) - 2 and nums[start] == startVal:
                start += 1
        return closest
