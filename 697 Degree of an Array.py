'''
697. Degree of an Array
https://leetcode.com/problems/degree-of-an-array/

Given a non-empty array of non-negative integers nums,
the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums,
that has the same degree as nums.

Example 1:

Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:

Input: [1,2,2,3,1,4,2]
Output: 6
'''
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:       
        
        book = {} # { n: [count, first appearance index of n]}
        res = [0, 0] # [degree, subarray size]
        
        for i, n in enumerate(nums):
            ct = 0 # count of n
            fi = i # first appearance index of n 
            if n in book:
                ct, fi = book[n]
            ct += 1
            book[n] = [ct, fi]
            
            subarraySize = i - fi + 1
            if ct > res[0]:
                res[0] = ct
                res[1] = subarraySize
            elif ct == res[0] and subarraySize < res[1]:
                res[1] = subarraySize
                
        return res[1]
