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
from functools import lru_cache

class Solution:
    @lru_cache(None)
    def topDown(self, i: int, j: int) -> int:
        # i, j are inclusive
        if i >= j:
            return 0
 
        return min(k + max(self.topDown(i, k-1), self.topDown(k+1, j)) for k in range(i, j+1))

    def getMoneyAmount(self, n: int) -> int:
        '''
        Let dp[i][j] represents minimum cost in range i...j inclusive,
        then dp[i][j] = min(k + max(dp[i][k-1], dp[k+1][j]) for k in [i...j])
        '''
        return self.topDown(1, n)
