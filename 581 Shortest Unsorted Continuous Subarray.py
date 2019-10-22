'''
581. Shortest Unsorted Continuous Subarray
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order,
then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
'''
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        end = None
        maxVal = nums[0]
        for i in range(1, len(nums)):
            maxVal = max(maxVal, nums[i])
            if nums[i] < maxVal:
                end = i
                
        start = None
        minVal = nums[len(nums)-1]
        for i in range(len(nums)-1, -1, -1):
            minVal = min(minVal, nums[i])
            if nums[i] > minVal:
                start = i
        
        return end - start + 1 if end is not None else 0
