'''
https://leetcode.com/problems/binary-watch
'''
def readBinaryWatch(n):
    res = []
    for i in xrange(12):
        for j in xrange(60):
            if bin((i << 6) + j).count('1') == n:
                res.append("{:d}:{:02d}".format(i,j))
    return res
