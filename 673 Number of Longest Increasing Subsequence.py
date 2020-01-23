'''
673. Number of Longest Increasing Subsequence
https://leetcode.com/problems/number-of-longest-increasing-subsequence/

Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1,
and there are 5 subsequences' length is 1, so output 5.

Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
'''
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        lens = [1] * size # max lengths
        counts = [1] * size # count of max lengths
        for i in range(size):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lens[i] == lens[j] + 1:
                        counts[i] += counts[j]
                    elif lens[i] < lens[j] + 1:
                        lens[i] = lens[j] + 1
                        counts[i] = counts[j]

        maxLen = 0
        maxCtr = 0
        for i in range(size):
            if lens[i] == maxLen:
                maxCtr += counts[i]
            elif lens[i] > maxLen:
                maxLen = lens[i]
                maxCtr = counts[i]

        return maxCtr
