from math import factorial
'''
Unique Paths
https://leetcode.com/problems/unique-paths/
'''
def comb(up,dn):
    return factorial(dn) / factorial(up) / factorial(dn - up)
    
def uniquePaths(self, m, n):
    return comb(m-1,(m+n)-2);
