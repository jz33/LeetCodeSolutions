'''
Count and Say
https://leetcode.com/problems/count-and-say/
'''
def countAndSay(self, n):
    res = "1"
    for _ in xrange(n - 1):
        res = self.iterative(res)
    return res

def iterative(self, n):
    count = 1
    i = 0
    res = ""
    while i < len(n) - 1:
        if n[i] == n[i+1]:
            count += 1
        else:
            res += str(count) + n[i]
            count = 1
        i += 1
    res += str(count) + n[i]
    return res
