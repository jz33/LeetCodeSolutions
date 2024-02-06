'''
346. Moving Average from Data Stream
https://leetcode.com/problems/moving-average-from-data-stream

Given a stream of integers and a window size,
calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

    MovingAverage(int size) Initializes the object with the size of the window size.
    
    double next(int val) Returns the moving average of the last size values of the stream.
   
Example 1:

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

Constraints:
    1 <= size <= 1000
    -105 <= val <= 105
    At most 104 calls will be made to next.
'''
from typing import List
import collections

class MovingAverage:
    '''
    Use deque
    '''
    def __init__(self, size: int):
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

class MovingAverage:
    '''
    Without deque
    '''
    def __init__(self, windowSize: int):
        self.windowSize = windowSize
        self.queue = []
        self.total = 0
        self.popIndex = 0 # where should start pop if queue is full

    def next(self, val: int) -> float:
        self.total += val
        if len(self.queue) < self.windowSize:
            self.queue.append(val)
        else:
            # pop
            self.total -= self.queue[self.popIndex]
            self.queue[self.popIndex] = val
            self.popIndex = (self.popIndex + 1) % self.windowSize
        return self.total / len(self.queue)

'''
Real facebook interview: moving average from array
https://www.1point3acres.com/bbs/thread-1043252-1-1.html
'''
def movingAverage(arr: List[int], winSize: int):
    if not winSize:
        return []
    
    result = []
    total = 0
    for i, e in enumerate(arr):
        # Extend
        total += e
        # Shrink
        if i >= winSize:
            total -= arr[i-winSize]
        # Result
        if i >= winSize - 1:
            result.append(total / winSize)
    return result

formula = [
    [1,2,3,4,5,6,7,8],
]
for f in formula:
    print('{0} equals {1}'.format(f, movingAverage(f, 4)))



 