'''
346. Moving Average from Data Stream
https://leetcode.com/problems/moving-average-from-data-stream/

Given a stream of integers and a window size,
calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = collections.deque()
        self.total = 0
        
    def next(self, val: int) -> float:
        self.total += val
        self.queue.append(val)
        if len(self.queue) > self.size:
            poped = self.queue.popleft()
            self.total -= poped
            
        return self.total / len(self.queue)
