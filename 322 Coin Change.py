'''
322. Coin Change
https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations and
an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

Constraints:
    1 <= coins.length <= 12
    1 <= coins[i] <= 231 - 1
    0 <= amount <= 104
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        
        # dp[i] is the minimum coin required to get amount i
        dp = [0] + [INF] * amount
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i-c] + 1)
    
        return dp[-1] if dp[-1] != INF else -1
