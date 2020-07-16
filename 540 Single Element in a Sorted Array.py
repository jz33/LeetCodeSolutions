'''
540. Single Element in a Sorted Array
https://leetcode.com/problems/single-element-in-a-sorted-array/

You are given a sorted array consisting of only integers where every element appears exactly twice,
except for one element which appears exactly once. Find this single element that appears only once.

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
        1 1 2 3 3 4 4 8 8
        0 1 2 3 4 5 6 7 8
        
        3 3 7 7 10 11 11
        0 1 2 3 4  5  6
        '''
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            
            # Make mid an even index
            mid = ((mid >> 1) << 1)

            # See example to understand
            if nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]
