class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        data = []
        cc = 0 # max column count
        data.append(v1)
        cc = max(len(v1),cc)
        data.append(v2)
        cc = max(len(v2),cc)
        self.data = data
        self.rc = 2
        self.cc = cc
        self.x = -1
        self.y = 0

    def next(self):
        """
        :rtype: int
        """
        return self.data[self.x][self.y]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.rc == 0 or self.cc == 0: return False
        data,cc,rc,x,y = self.data,self.cc,self.rc,self.x,self.y

        while y < cc:
            if x == rc - 1:
                x = 0
                y += 1
            else:
                x += 1
            if y < len(data[x]):
                self.x,self.y = x,y
                return True
        return False
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
