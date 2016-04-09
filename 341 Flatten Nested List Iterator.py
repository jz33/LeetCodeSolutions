class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.p = nestedList
        self.i = 0
        self.stack = []
        self.nextElement = None

    def next(self):
        """
        :rtype: int
        """
        return self.nextElement
        
    def hasNext(self):
        """
        :rtype: bool
        """
        while self.i < len(self.p) or len(self.stack) > 0:
            if self.i < len(self.p):
                e = self.p[self.i]
                if e.isInteger():
                    self.i = self.i + 1
                    self.nextElement = e.getInteger()
                    return True
                else:
                    self.stack.append((self.p, self.i + 1))
                    self.p = e.getList()
                    self.i = 0
            else:
                self.p,self.i = self.stack.pop()
        return False
