'''
75. Sort Colors
https://leetcode.com/problems/sort-colors/solution/
Given an array with n objects colored red, white or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:  
        zi = 0 # destination index for '0'
        ti = len(nums) - 1 # destination index for '2'
        i = 0
        while i <= ti:
            if nums[i] == 0:
                # Put '0' to left
                nums[i], nums[zi] =  nums[zi], nums[i]
                i += 1
                zi += 1
                # Increase i here, if i == zi, nums[i] is 0,
                # and if i > zi, nums[i] is 1              
            elif nums[i] == 1:
                i += 1
            else: # nums[i] == 2
                # Put '2' to right
                nums[i], nums[ti] =  nums[ti], nums[i]
                ti -= 1
                # Cannot increse i here, because nums[i] could be 2
