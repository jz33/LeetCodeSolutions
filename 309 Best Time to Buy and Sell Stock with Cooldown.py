from sys import maxint
'''
Best Time to Buy and Sell Stock with Cooldown
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
'''
def withCooldown(prices):
    if len(prices) < 2: return 0
    sold = [0]*3
    bought = [-maxint-1]*2
    for i,p in enumerate(prices):
        s = i % 3
        b = i % 2
        sold[s] = max(sold[s-1],bought[b-1]+p)
        bought[b] = max(bought[b-1],sold[s-2]-p)
    return sold[(len(prices)-1) % 3]
