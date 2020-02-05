'''
829. Consecutive Numbers Sum
https://leetcode.com/problems/consecutive-numbers-sum/

Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.
'''
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        '''
        (a + a + b - 1) * b // 2 = N
        a = N / b - (b - 1) / 2
        '''
        count = 1
        for b in range(2, N):
            a = N / b - (b - 1) / 2
            if a < 1.0:
                break
            if a.is_integer():
                count += 1
        return count
