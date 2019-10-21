'''
322. Coin Change
https://leetcode.com/problems/coin-change/

You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: 
        # Be careful when amount == 0
        INF = (amount + 1) * 2
        dp = [INF] * (amount+1)
        dp[0] = 0
        
        for c in coins:
            for i in range(c,amount+1):
                dp[i] = min(dp[i], dp[i-c] + 1)
    
        return dp[-1] if dp[-1] != INF else -1
