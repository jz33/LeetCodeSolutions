'''
446. Arithmetic Slices II - Subsequence
https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

A sequence of numbers is called arithmetic if it consists of at least three elements and
if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic.

1, 1, 2, 5, 7
 
A zero-indexed array A consisting of N numbers is given. A subsequence slice of that array is
any sequence of integers (P0, P1, ..., Pk) such that 0 ≤ P0 < P1 < ... < Pk < N.

A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic if the sequence
A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. In particular, this means that k ≥ 2.

The function should return the number of arithmetic subsequence slices in the array A.

The input contains N integers. Every integer is in the range of -231 and 231-1 and 0 ≤ N ≤ 1000.
The output is guaranteed to be less than 231-1.

 
Example:

Input: [2, 4, 6, 8, 10]

Output: 7

Explanation:
All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
'''
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if not A or len(A) < 3:
            return 0
    
        # dp[i] = {arithmetic subsequence diff : count ending at i}
        dp = [collections.Counter() for _ in range(len(A))]
        total = 0
        for i in range(1, len(A)):
            for j in range(i-1, -1, -1):
                diff = A[i] - A[j]
                c0 = dp[j][diff]
                
                # The number of arithmetic subsequence before i
                # with diff is c0, so total should add c0, because
                # with A[i] new size + 1 subsequences of diff are created.
                total += c0
                
                # However, the count of subsequence ending on i
                # with diff should just increase by 1. These sequences are
                # not necessarily size >= 3, so cannot add to total yet.
                dp[i][diff] += c0 + 1
                
        return total
