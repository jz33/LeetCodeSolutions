'''
154. Find Minimum in Rotated Sorted Array II
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
'''
class Solution:
    def findMin(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        
        while left < right:
            mid = left + ((right - left) >> 1)
            
            if arr[mid] > arr[right]:
                left = mid + 1          
            elif arr[mid] < arr[right]:
                right = mid      
            else:
                right -= 1
  
        return arr[left]
