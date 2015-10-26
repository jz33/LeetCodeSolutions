class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        data = []
        for row in vec2d:
            if len(row) > 0:
                data.append(row)
        self.data = data
        self.R = len(data)
        self.i = 0
        self.j = 0

    def next(self):
        """
        :rtype: int
        """
        d = self.data[self.i][self.j]
        if self.j == len(self.data[self.i])-1:
            self.i += 1
            self.j = 0
        else:
            self.j += 1
        return d
            
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < self.R - 1 or self.i == self.R - 1 and self.j < len(self.data[-1])
