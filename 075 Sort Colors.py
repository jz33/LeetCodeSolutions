'''
75. Sort Colors
https://leetcode.com/problems/sort-colors/solution/

Given an array nums with n objects colored red, white, or blue, sort them in-place so that
objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:  
        left = 0 # destination index for '0'
        right = len(nums) - 1 # destination index for '2'
        i = 0
        while i <= right:
            if nums[i] == 0:
                # Put '0' to left
                nums[i], nums[left] =  nums[left], nums[i]
                i += 1
                left += 1
            elif nums[i] == 1:
                i += 1
            else: # nums[i] == 2
                # Put '2' to right
                nums[i], nums[right] =  nums[right], nums[i]
                right -= 1
                # Cannot increase i here, because nums[i] could be 2
