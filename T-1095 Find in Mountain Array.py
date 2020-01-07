'''
1095. Find in Mountain Array
https://leetcode.com/problems/find-in-mountain-array/

(This problem is an interactive problem.)

You may recall that an array A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.
If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.

Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.
Also, any solutions that attempt to circumvent the judge will result in disqualification.

Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
 

Constraints:

3 <= mountain_arr.length() <= 10000
0 <= target <= 10^9
0 <= mountain_arr.get(index) <= 10^9
'''
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findPeak(self, left: int, right: int, mountain_arr: 'MountainArray') -> int:
        while left < right:
            mid = left + (right - left) // 2
            midVal = mountain_arr.get(mid)
            midValPlus1 = mountain_arr.get(mid+1)
            
            if midVal < midValPlus1:
                left = mid + 1
            else: # midVal > midValPlus1
                right = mid
                
        return left
            
    def binarySearch(self, target: int, left: int, right: int, ascending: bool, mountain_arr: 'MountainArray') -> int:
        while left <= right:
            mid = left + (right - left) // 2
            midVal = mountain_arr.get(mid)
            
            if midVal == target:
                return mid
            elif midVal < target:
                if ascending:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if ascending:
                    right = mid - 1
                else:
                    left = mid + 1
                
        return -1
      
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        size = mountain_arr.length()
        leftMost = mountain_arr.get(0)
        rightMost = mountain_arr.get(size-1)
        
        if target < min(leftMost, rightMost):
            return -1
        elif target == leftMost:
            return 0
        
        peakIndex = self.findPeak(0, size-1, mountain_arr)
        peakValue = mountain_arr.get(peakIndex)
        
        if target > peakValue:
            return -1
        elif target == peakValue:
            return peakIndex

        # The question needs smallest index, so search left section first
        res = self.binarySearch(target, 0, peakIndex, True, mountain_arr)
        if res == -1:
            res = self.binarySearch(target, peakIndex+1, size-1, False, mountain_arr)                
        return res      
