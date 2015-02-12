import random,sys
'''
121 Best Time to Buy and Sell Stock
122 Best Time to Buy and Sell Stock II
123 Best Time to Buy and Sell Stock III
https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/
https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
'''
# 121
def singleTrade(prices):
    if len(prices) < 2: print "len(prices) < 2"

    start = 0; ended = 0; profit = 0 # result vars
    lo = 0; # tracing var

    print "prices: {}\n".format(prices)
    
    # append min int for last transaction
    prices.append(-1)
    
    for i in range(1,len(prices)):
        if prices[i] < prices[i-1]:
            # update from previous
            p = prices[i-1] - prices[lo]
            if p > profit:
                start = lo
                ended = i-1
                profit = p
                
            # update current
            if prices[i] < prices[lo]: lo = i

    print "start: {}, ended: {}, profit: {}\n\n".format(start,ended,profit)

# 122
def multiTrades(prices):
    if len(prices) < 2: print "len(prices) < 2"

    profit = 0;lo = 0; 
    print "prices: {}\n".format(prices)
    
    # append min int for last transaction
    prices.append(-1)
    
    for i in range(1,len(prices)):
        if prices[i] < prices[i-1]:
            profit += prices[i-1] - prices[lo]
            lo = i

    print "profit: {}\n\n".format(profit)

# 123
def towTrades(prices):
    if len(prices) < 2: print "len(prices) < 2"

    profit = 0 ; leftEnd = 0; # result vars
    hi =0; lo = 0; # tracing var
    
    print "prices: {}\n".format(prices)
    
    # compute max profit of single trade from 0 to each index,
    # as if that index is the last day
    # similar as "singleTrade"
    mp = [0]
    prices.append(-1)
    lo = 0
    for i in range(1,len(prices)):
        if prices[i] < prices[lo]: 
            lo = i
            mp.append(mp[i-1])
        else:
            mp.append(max(mp[i-1],prices[i] - prices[lo]))

    # compute 2nd trade from prices[-3] to front
    prices.pop()
    profit = mp[-1]
    leftEnd = len(prices) - 1
    hi = lo = -2
    
    if prices[-1] > prices[-2]:
        hi = -1
        p = mp[-3] + prices[hi] - prices[lo]
        if p > mp[-1]:
            profit = p
            leftEnd = len(prices) - 3
    
    prices = [-1] + prices
    for i in range(-3,-len(prices),-1):
        if prices[i] > prices[hi]:
            hi = lo = i
        elif prices[i] < prices[lo]:
            lo = i
            p = mp[i-1] + prices[hi] - prices[lo]
            if p > profit:
                profit = p
                leftEnd = i - 1
    
    print "mp: {}".format(mp)
    print "profit: {}, leftEnd: {}\n\n".format(profit, leftEnd)
        
    
def simpleTest(func):
    print func.__name__
    
    prices = [4,4,4,4,4] # flat
    func(prices)
    
    prices = [] # ascending
    for i in range(0,10): prices.append(i*2+1)
    func(prices)
    
    prices = [] # descending
    for i in range(10,0,-1): prices.append(i*2+1)
    func(prices)
    
    prices = [4,10,2,3,4] # not lowest as start
    func(prices)

    prices = [] # random
    for i in range(0,10): prices.append(random.randint(1,30))
    func(prices)
    
def main():
    simpleTest(singleTrade)
    simpleTest(multiTrades)
    simpleTest(towTrades)
    
if __name__ == "__main__":
    main()
