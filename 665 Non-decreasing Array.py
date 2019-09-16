'''
665. Non-decreasing Array
https://leetcode.com/problems/non-decreasing-array/

Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:

Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:

Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
'''
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # Count of ascending subarray
        c = 0
        # Index of first break point
        b = -1
        for i, e in enumerate(nums):
            if i > 0 and e < nums[i-1]:
                c += 1
                b = i
            if c > 1:
                return False   
                
        if c == 0:
            return True
        
        # Try modify nums[b] to nums[b-1] 
        # or mofidy nums[b-1] to nums[b]
        # b and b-1 must exist
        return (b + 1 >= len(nums) or nums[b-1] <= nums[b+1]) or (b - 2 < 0 or nums[b] >= nums[b-2])
