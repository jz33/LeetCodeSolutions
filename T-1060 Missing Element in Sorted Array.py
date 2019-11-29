'''
1060. Missing Element in Sorted Array
https://leetcode.com/problems/missing-element-in-sorted-array/

Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.

Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.

Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
'''
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        N = len(nums)
        # Find the largest index in nums where the missing numbers
        # before it is less than k
        upperBound = 0 
        left = 0
        right = N-1
        while left <= right:
            mid = left + (right - left) // 2
            # How many missing elements before nums[mid] ?
            missed = nums[mid] - nums[0] - mid
            if missed < k:
                upperBound = mid
                left = mid + 1
            else:
                right = mid - 1
        return k + nums[0] + upperBound
