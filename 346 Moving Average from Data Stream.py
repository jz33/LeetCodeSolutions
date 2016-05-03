'''
Moving Average from Data Stream
https://leetcode.com/problems/moving-average-from-data-stream/
'''
from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.dq = deque()
        self.size = size
        self.avg = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        total = self.avg * len(self.dq)
        if len(self.dq) == self.size:
            total -= self.dq.popleft()
        self.dq.append(val)
        total += val
        self.avg = total / float(len(self.dq))
        return self.avg
        
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
