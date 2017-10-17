"""
Coin Change 2
https://leetcode.com/problems/coin-change-2
Same as 039 Combination Sum
"""
def change(self, amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    buf = [0] * (amount + 1)
    buf[0] = 1
    for c in coins:
        for i in xrange(c,amount+1):
            buf[i] += buf[i-c]
    return buf[amount]
