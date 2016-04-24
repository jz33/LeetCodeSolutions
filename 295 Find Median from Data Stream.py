from heapq import heappush, heappop, heappushpop
'''
Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/
'''
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small = []
        self.large = []        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small,-num))
        else: # len(self.small) + 1 == len(self.large):
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return (float(self.large[0]) - float(self.small[0])) / 2.0
        else: # len(self.small) + 1 == len(self.large):
            return self.large[0]


obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print obj.findMedian()
obj.addNum(3) 
print obj.findMedian()
