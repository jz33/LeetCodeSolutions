'''
718. Maximum Length of Repeated Subarray
https://leetcode.com/problems/maximum-length-of-repeated-subarray/

Given two integer arrays nums1 and nums2,
return the maximum length of a subarray that appears in both arrays.

Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
Explanation: The repeated subarray with maximum length is [0,0,0,0,0].

Constraints:
    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 100
'''
def longestCommonString(nums1, nums2) -> int:
    '''
    Classic longest common substring problem
    '''
    dp = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]
    maxLength = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
                maxLength = max(maxLength, dp[i+1][j+1])
    return maxLength

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        return longestCommonString(nums1, nums2)

