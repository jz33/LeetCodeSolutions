'''
209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray
whose sum is greater than or equal to target.

If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 104
 
Follow up: If you have figured out the O(n) solution,
try coding another solution of which the time complexity is O(n log(n)).
'''
class SlidingWindow:
    def __init__(self):
        self.windowSum = 0
    
    def isValid(self, target: int) -> bool:
        return self.windowSum >= target
    
    def add(self, val: int):
        self.windowSum += val
    
    def remove(self, val: int):
        self.windowSum -= val

class Solution:
    '''
    Similar pattern to 76. Minimum Window Substring
    '''
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = SlidingWindow()
        left = 0
        minLength = len(nums) + 1
        for right, val in enumerate(nums):
            # Expand
            window.add(val)
            while window.isValid(target) and left <= right: 
                # Update result
                minLength = min(minLength, right + 1 - left)
                # Shrink
                window.remove(nums[left])
                left += 1
        return minLength if minLength < len(nums) + 1 else 0