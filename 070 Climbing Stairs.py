'''
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        This is essentially Fibonacci number
        '''
        if n == 0:
            return 0
        
        dp = [1,None,0]
        for i in range(1, n+1):
            di = i % 3
            dp[di] = dp[di-1] + dp[di-2]
            
        return dp[n % 3]
