'''
852. Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/

Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1

Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
'''
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        '''
        Same question to Find Peak Element
        '''
        left = 0
        right = len(A) - 1
        while left < right:
            mid = left + (right - left) // 2
            if A[mid] > A[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left
