"""
Ones and Zeroes
https://leetcode.com/problems/ones-and-zeroes/
"""
def findMaxForm(self, strs, m, n):
    """
    :type strs: List[str]
    :type m: int
    :type n: int
    :rtype: int
    """
    buf = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
    for s in strs:
        ones = sum(1 for c in s if c == "1")
        zeros = len(s) - ones
        for i in xrange(m, zeros-1, -1):
            for j in xrange(n, ones-1, -1):
                buf[i][j] = max(buf[i][j], buf[i-zeros][j-ones] + 1)
    return buf[m][n]
