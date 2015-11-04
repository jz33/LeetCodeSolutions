from copy import deepcopy
from sys import argv
'''
Factor Combinations
https://leetcode.com/problems/factor-combinations/

Backtracking
'''
pool = []

def rec(n,row,start):
    for i in xrange(start,n / 2 + 1):
        if n % i == 0:
            row.append(i)
            rec(n / i, row, i)
            row.pop()  
    if len(row) > 0 and n >= row[-1]:
        pool.append(deepcopy(row+[n]))
            
def getFactors(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    del pool[:]
    rec(n,[],2)
    return pool
    
r = getFactors(int(argv[1]))
print r
