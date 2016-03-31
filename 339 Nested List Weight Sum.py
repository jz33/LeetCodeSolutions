'''
Nested List Weight Sum
https://leetcode.com/problems/nested-list-weight-sum/
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if len(nestedList) == 0: return 0
        s = 0 # sum
        d = 1 # depth
        i = 0
        p = nestedList
        stack = []
        while i < len(p) or len(stack) > 0:
            if i < len(p):
                e = p[i]
                if e.isInteger():
                    s += e.getInteger() * d
                    i += 1
                else:
                    stack.append((p,i+1))
                    p = e.getList()
                    i = 0
                    d += 1
            else:
                p, i = stack.pop()
                d -= 1
        return s
