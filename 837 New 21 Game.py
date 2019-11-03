'''
837. New 21 Game
https://leetcode.com/problems/new-21-game/

Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.
During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.
Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?

Example 1:

Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.
Example 2:

Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
Example 3:

Input: N = 21, K = 17, W = 10
Output: 0.73278
'''
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0 or N >= K + W: return 1.0
        
        # dp[i] is the possibily to reach i
        dp = [0.0] * (N+1)
        dp[0] = 1.0
        
        # An O(N^2) approach
        # for i in range(1, N+1):
        #     for j in range(max(0,i-W),min(i,K)):
        #         dp[i] += dp[j] / float(W)
        # Notice the 2nd loop'sum can be cached,
        # So there is an O(N) approach

        ws = 1.0 # window sum, last W dp values' sum
        for i in range(1, N+1):
            dp[i] = ws / float(W)
            if i < K:
                ws += dp[i]
            if i - W >= 0:
                ws -= dp[i-W]

        return sum(dp[K:])
