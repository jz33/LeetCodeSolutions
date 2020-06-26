'''
978. Longest Turbulent Subarray
https://leetcode.com/problems/longest-turbulent-subarray/

A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between
each adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.

Example 1:

Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])

Example 2:

Input: [4,8,12,16]
Output: 2

Example 3:

Input: [100]
Output: 1

Note:

1 <= A.length <= 40000
0 <= A[i] <= 10^9
'''
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) < 2:
            return len(A)
        
        # 0: undetermined,
        # 1: going up
        # 2: going down
        trend = 0
        maxLength, length = 1, 1
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                maxLength = max(maxLength, length)
                length = 1
                trend = 0
            elif A[i] > A[i-1]:
                if trend == 0 or trend == -1:
                    length += 1
                else:
                    maxLength = max(maxLength, length)
                    length = 2
                trend = 1
            else: # A[i] < A[i-1]
                if trend == 0 or trend == 1:
                    length += 1
                else:
                    maxLength = max(maxLength, length)
                    length = 2
                trend = -1
                
        return max(maxLength, length)
