'''
1043. Partition Array for Maximum Sum
https://leetcode.com/problems/partition-array-for-maximum-sum/

Given an integer array arr, partition the array into (contiguous) subarrays of length at most k.
After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.
Test cases are generated so that the answer fits in a 32-bit integer.

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]

Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83

Example 3:

Input: arr = [1], k = 1
Output: 1

Constraints:
    1 <= arr.length <= 500
    0 <= arr[i] <= 109
    1 <= k <= arr.length
'''
class Solution:
    '''
    T(i) = max(arr[i] + T[i-1], max(arr[i], arr[i-1]) * 2 + T[i-2], max(arr[i], arr[i-1], arr[i-2]) * 3 + T[i-3], ...))
    '''
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr)+1) # dp[i] is the maximun result ending in arr[:i]
        for i in range(len(arr)):
            maxVal = 0
            for j in range(min(k, i+1)):
                maxVal = max(maxVal, arr[i-j])
                dp[i+1] = max(dp[i+1], maxVal * (j+1) + dp[i-j])
        return dp[-1]