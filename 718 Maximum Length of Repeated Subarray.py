'''
718. Maximum Length of Repeated Subarray

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3

Explanation: 
The repeated subarray with maximum length is [3, 2, 1]
'''
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        len_A = len(A)
        len_B = len(B)
        
        # buf[i][j] means the longest commong subarray which ends on 
        # A[i] and B[j]
        buf = [[0] * (len_B+1) for _ in range(len_A+1)]
        
        maxLength = 0
        for i in range(1, len_A+1):
            for j in range(1, len_B+1):
                if A[i-1] == B[j-1]:
                    buf[i][j] = buf[i-1][j-1] + 1
                    maxLength = max(maxLength, buf[i][j])
                    
        return maxLength
