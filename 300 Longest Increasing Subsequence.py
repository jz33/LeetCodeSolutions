'''
300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''
class Solution:
    def getInsertionPoint(self, arr: List[int], tag: int) -> int:
        # Get insertion point of tag in arr who is ascendingly sorted       
        left = 0
        right = len(arr) - 1       
        while left <= right:
            mid = left + ((right - left) >> 1)
            if arr[mid] == tag:
                return mid
            elif arr[mid] < tag:
                left = mid + 1
            else:
                right = mid - 1
        return left
      
    def lengthOfLIS(self, nums: List[int]) -> int:        
        # arr is ascending
        arr = []
        for n in nums:
            ip = self.getInsertionPoint(arr, n)
            if ip > len(arr) - 1:
                # If n is bigger than everyone in arr, append it
                arr.append(n)
            else:
                # Else, replace arr[ip] with n, because n <= arr[ip]
                # And we want to be greedy the let arr[i] smaller
                arr[ip] = n
        return len(arr)
