'''
1031. Maximum Sum of Two Non-Overlapping Subarrays
https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays,
which have lengths L and M.  (For clarification, the L-length subarray could occur before or after the M-length subarray.)

Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:

    0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
    0 <= j < j + M - 1 < i < i + L - 1 < A.length.

 

Example 1:

Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.

Example 2:

Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.

Example 3:

Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
'''
class Solution:
    def getDp(self, A: List[int], width: int, dpSize: int):
        '''
        dp[i] is the max sum subarray of width in A[:i+width]
        '''
        dp = [0] * dpSize
        subarraySum = sum(A[:width])
        dp[0] = subarraySum
        for i in range(len(dp)-1):
            subarraySum = subarraySum - A[i] + A[i+width]
            dp[i+1] = max(dp[i], subarraySum)
        return dp
    
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        # At index i, needs to know the max sum of L sized subarray
        # in A[:i], A[i:], and max sum of M sized subarray in A[:i], A[i:]
        # Need to pre-compute 4 dp arrays.
        # Their sizes are all the same
        dpSize = len(A) - L - M + 1
        dpLeftL = self.getDp(A, L, dpSize)
        dpRightM = self.getDp(A[L:][::-1], M, dpSize)
        dpLeftM = dpLeftL if M == L else self.getDp(A, M, dpSize)
        dpRightL = dpRightM if M == L else self.getDp(A[M:][::-1], L, dpSize)

        # A combination is dpLeftL[i] + dpRightM[-i-1]
        return max(max(dpLeftL[i] + dpRightM[-i-1], dpLeftM[i] + dpRightL[-i-1]) for i in range(dpSize))
