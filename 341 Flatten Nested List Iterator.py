'''
341. Flatten Nested List Iterator
https://leetcode.com/problems/flatten-nested-list-iterator/

You are given a nested list of integers nestedList.
Each element is either an integer or a list whose elements may also be integers or other lists.
Implement an iterator to flatten it.

Implement the NestedIterator class:

    NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
    int next() Returns the next integer in the nested list.
    boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res

If res matches the expected flattened list, then your code will be judged as correct.

Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:

Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

Constraints:
    1 <= nestedList.length <= 500
    The values of the integers in the nested list is in the range [-106, 106].
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
        self.value = None
        self.list = nestedList # a list points to list of a nestestList
        self.position = 0
        self.stack = [] # [(list, next position)]
        
    def next(self) -> int:
        '''
        Will call hasNext first then call this
        '''
        return self.value
    
    def hasNext(self) -> bool:
        while self.position < len(self.list) or self.stack:
            if self.position < len(self.list):
                node = self.list[self.position]
                if node.isInteger():
                    self.position = self.position + 1
                    self.value = node.getInteger()
                    return True
                else:
                    self.stack.append((self.list, self.position + 1))
                    self.list = node.getList()
                    self.position = 0
            else:
                self.list, self.position = self.stack.pop()
        return False
