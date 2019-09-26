/*
34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
*/
class Solution:
    '''
    O(log(N))
    '''
    def findLeftBound(self, nums: List[int], target: int) -> int:
        '''
        Find left bound (the smallest index) of nums who equals to target
        '''
        left = 0
        right = len(nums) - 1
    
        bound = -1
        while left <= right:
            mid = left + ((right - left) >> 1)
            e = nums[mid]
            if e == target:
                bound = mid
                right = mid - 1
            elif e > target:
                right = mid - 1
            else:
                left = mid + 1
        return bound
                
    def findRightBound(self, nums: List[int], target: int) -> int:
        '''
        Find right bound (the largest index) of nums who equals to target
        '''
        left = 0
        right = len(nums) - 1
    
        bound = -1
        while left <= right:
            mid = left + ((right - left) >> 1)
            e = nums[mid]
            if e == target:
                bound = mid
                left = mid + 1
            elif e > target:
                right = mid - 1
            else:
                left = mid + 1
        return bound
                
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.findLeftBound(nums, target), self.findRightBound(nums, target)]
