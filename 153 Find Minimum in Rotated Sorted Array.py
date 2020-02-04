'''
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1

Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

Example 3:
Input: [1,2,3]
Output: 1

Example 4:
Input: [0]
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
