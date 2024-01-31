'''
697. Degree of an Array
https://leetcode.com/problems/degree-of-an-array/

Given a non-empty array of non-negative integers nums,
the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums,
that has the same degree as nums.

Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

Constraints:
    nums.length will be between 1 and 50,000.
    nums[i] will be an integer between 0 and 49,999.
'''
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:       
        book = {} # { value : (count of the value, first appearance index of the value)}
        degree = 0
        minSubarraySize = len(nums)       
        for i, val in enumerate(nums):
            count, first = book.get(val, (0, i))
            count += 1
            book[val] = (count, first)
            
            # Check the array with val as the degree
            # No need to find the maximum degree as the loop can find that
            subarraySize = i - first + 1
            if count > degree:
                degree = count
                minSubarraySize = subarraySize
            elif count == degree and subarraySize < minSubarraySize:
                minSubarraySize = subarraySize
                
        return minSubarraySize
