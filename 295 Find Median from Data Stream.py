'''
295. Find Median from Data Stream

Median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 
Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 
Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
'''
from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):     
        # Either these 2 heaps have same # of elements
        # Or minHeap has 1 more element than maxHeap
        self.maxHeap = [] # negatives
        self.minHeap = [] 

    def addNum(self, n: int) -> None:
        maxHeap = self.maxHeap
        minHeap = self.minHeap
        
        if len(maxHeap) == len(minHeap):
            heappush(maxHeap, -n)
            p = -heappop(maxHeap)
            heappush(minHeap, p)           
        else:
            heappush(minHeap, n)
            p = heappop(minHeap)
            heappush(maxHeap, -p)

    def findMedian(self) -> float:
        maxHeap = self.maxHeap
        minHeap = self.minHeap
        
        if len(maxHeap) == len(minHeap):
            return float(-maxHeap[0] + minHeap[0]) / 2.0
        else:
            return float(minHeap[0])
