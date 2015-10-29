import re
'''
Flip Game II
https://leetcode.com/problems/flip-game-ii/
O(N^2)
'''
'''
Sprague-Grundy Theorem Solution:
https://leetcode.com/discuss/64344/theory-matters-from-backtracking-128ms-to-dp-0ms
'''
class solution(object):
    prev = {}
    pattern = re.compile(r'\+\++')
    
    def canWin(self,input):
        ls = tuple(map(len, self.pattern.findall(input)))
        return self.rec(ls)
        
    def rec(self,ls):
        tup = tuple(sorted(e for e in ls if e > 1))
        if tup not in self.prev:
            can = False
            for i,v in enumerate(tup):
                for j in xrange(v - 1):
                    if self.rec(tup[:i] + (j,v-2-j) + tup[i+1:]) == False:
                        can = True
                        break
            self.prev[tup] = can
            print tup, can
        return self.prev[tup]
