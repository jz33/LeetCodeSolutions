'''
Search Insert Position
https://oj.leetcode.com/problems/search-insert-position/

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''
class Solution:
    def searchInsert(self, arr: List[int], tag: int) -> int:
        left = 0
        right = len(arr) - 1       
        while left <= right:
            mid = left + ((right - left) >> 1)
            if arr[mid] == tag:
                return mid
            elif arr[mid] < tag:
                left = mid + 1
            else:
                right = mid - 1      
        return left
