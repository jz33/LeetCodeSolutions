'''
34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109
'''
def getLowerBound(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    bound = None
    while left <= right:
        mid = (left + right) >> 1
        midVal = nums[mid]
        if midVal < target:
            left = mid + 1
        elif midVal == target:
            bound = mid
            right = mid - 1
        else:
            right = mid - 1
    return -1 if bound is None else bound

def getUpperBound(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    bound = None
    while left <= right:
        mid = (left + right) >> 1
        midVal = nums[mid]
        if midVal < target:
            left = mid + 1
        elif midVal == target:
            bound = mid
            left = mid + 1
        else:
            right = mid - 1
    return -1 if bound is None else bound

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [getLowerBound(nums, target), getUpperBound(nums, target)]
