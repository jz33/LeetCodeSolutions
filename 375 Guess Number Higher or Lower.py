'''
375 Guess Number Higher or Lower
https://leetcode.com/problems/guess-number-higher-or-lower-ii

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x.
You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
'''
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp is (n+1) * (n+1) matrix
        # dp[i][j] is the min value of i...j inclusive
        # dp[i][i] is alwasy 0
        dp = [[0] * (n+1) for _ in range(n+1)]

        # left + stride = right <= n
        for stride in range(1, n+1):
            # left + stride = right <= n
            for left in range(0, n-stride+1):
                right = left + stride
                
                # i is the number to guess
                # left < i < right
                # Clearly, no need to guess right,
                # then maximum possible guess is (right-1)* stride
                minVal = (right - 1) * stride
                for i in range(left+1, right):
                    minVal = min(minVal, max(dp[left][i-1], dp[i+1][right]) + i)

                dp[left][right] = minVal

        return dp[0][n]
