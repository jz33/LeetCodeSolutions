"""
518. Coin Change 2
https://leetcode.com/problems/coin-change-2/

You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10] 
Output: 1

This question can be asked in different way:
https://leetcode.com/discuss/interview-question/414064/Google-or-Count-Integer-Partitions

Given a positive integer n, find out how many ways of writing n as a sum of positive integers.
Two sums that differ only in the order of their summands are considered the same partition.

Example:

Input: 5
Output: 6
Explanation:
1. 1 + 1 + 1 + 1 + 1
2. 1 + 1 + 1 + 2
3. 1 + 1 + 3
4. 1 + 4
5. 1 + 2 + 2
6. 2 + 3
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Same as 039 Combination Sum
        dp = [1] + [0] * amount
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i-c]
        return dp[-1]
