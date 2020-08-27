'''
341. Flatten Nested List Iterator
https://leetcode.com/problems/flatten-nested-list-iterator/

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].

Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.value = None # next integer
        self.list = nestedList # a list points to list of a nestestList
        self.pos = 0 # position in self.list
        self.stack = [] # [(list, position)]
        
    def next(self) -> int:
        '''
        Will call hasNext first then call this
        '''
        return self.value
    
    def hasNext(self) -> bool:
        while self.pos < len(self.list) or self.stack:
            if self.pos < len(self.list):
                e = self.list[self.pos]
                if e.isInteger():
                    self.pos = self.pos + 1
                    self.value = e.getInteger()
                    return True
                else:
                    self.stack.append((self.list, self.pos + 1))
                    self.list = e.getList()
                    self.pos = 0
            else:
                self.list, self.pos = self.stack.pop()
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
