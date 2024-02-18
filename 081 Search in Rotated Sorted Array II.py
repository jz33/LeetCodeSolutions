'''
81. Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target,
return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Constraints:
    1 <= nums.length <= 5000
    -104 <= nums[i] <= 104
    nums is guaranteed to be rotated at some pivot.
    -104 <= target <= 104

Follow up: This problem is similar to Search in Rotated Sorted Array,
but nums may contain duplicates. Would this affect the runtime complexity? How and why?

'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        # Make sure left most != right most
        # This is the key difference to 33. Search in Rotated Sorted Array
        while left < right and nums[left] == nums[right]:
            right -= 1
        lastVal = nums[right]
        
        # If target is bigger than last value, it is on left branch
        targetIsOnLeft = target > lastVal
        
        while left <= right:
            mid = left + (right - left) // 2
            midVal = nums[mid]            
            if midVal == target:
                return True
            
            # Whether middle value is on left or right
            middleIsOnLeft = midVal > lastVal

            if targetIsOnLeft and middleIsOnLeft and midVal < target or\
                not targetIsOnLeft and not middleIsOnLeft and midVal < target or\
                not targetIsOnLeft and middleIsOnLeft:
                left = mid + 1
            else:
                right = mid - 1

        return False
