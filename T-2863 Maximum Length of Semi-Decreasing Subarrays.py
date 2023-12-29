'''
2863. Maximum Length of Semi-Decreasing Subarrays
https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

You are given an integer array nums.

Return the length of the longest semi-decreasing subarray of nums,
and 0 if there are no such subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.
A non-empty array is semi-decreasing if its first element is strictly greater than its last element.

Example 1:

Input: nums = [7,6,5,4,3,2,1,6,10,11]
Output: 8
Explanation: Take the subarray [7,6,5,4,3,2,1,6].
The first element is 7 and the last one is 6 so the condition is met.
Hence, the answer would be the length of the subarray or 8.
It can be shown that there aren't any subarrays with the given condition with a length greater than 8.

Example 2:

Input: nums = [57,55,50,60,61,58,63,59,64,60,63]
Output: 6
Explanation: Take the subarray [61,58,63,59,64,60].
The first element is 61 and the last one is 60 so the condition is met.
Hence, the answer would be the length of the subarray or 6.
It can be shown that there aren't any subarrays with the given condition with a length greater than 6.
Example 3:

Input: nums = [1,2,3,4]
Output: 0
Explanation: Since there are no semi-decreasing subarrays in the given array, the answer is 0.
 
Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        '''
        Assume the subarray (i,j) both inclusive is the answer,
        then for any i` < i, there should not be nums[i'] > nums[i] (if so, i' should be the answer).
        To get all possible left bound of the final answer, this hints a ascending monotonic queue,
        where for q[i], it is the largest number in nums[:i].
        For right bound, similarly, there cannot be a j' where j' > j and nums[j'] < nums[j].
        This indicates another ascending monotonic queue, where q[i] is the smallest in nums[i:].
        For given example [7,6,5,4,3,2,1,6,10,11],
        left queue: [7,10,11],
        right queue: [1,6,10,11].
        For [57,55,50,60,61,58,63,59,64,60,63],
        left queue: [57,60,61,63,64],
        right queue: [50,58,59,60,63].
        The left bound of the answer must be from left queue, the right bound must be from right queue.
        Comparing the 2 queues can get the answer
        '''
        leftQueue = [0]
        for i in range(1, len(nums)):
            if nums[i] > nums[leftQueue[-1]]:
                leftQueue.append(i)
        
        # Early return, if no descending trend at all
        if len(leftQueue) == len(nums):
            return 0

        rightQueue = [len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[rightQueue[-1]]:
                rightQueue.append(i)
                
        rightQueue.reverse()

        left = 0 
        right = 0
        maxLen = 0
        while left < len(leftQueue) and right < len(rightQueue):
            if leftQueue[left] >= rightQueue[right]:
                # Left index is after right index, increase right index
                right += 1
            elif nums[leftQueue[left]] <= nums[rightQueue[right]]:
                # Left value is not greater than right value, increase left index
                left += 1
            else:
                # Valid. Increase right to get better answer
                maxLen = max(maxLen, rightQueue[right] - leftQueue[left] + 1)
                right += 1
        return maxLen


