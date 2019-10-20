'''
759. Employee Free Time
https://leetcode.com/problems/employee-free-time/

We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]

Explanation:
There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.

Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
'''
from heapq import heappush, heappop
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class HeapNode:
    def __init__(self, interval):
        self.start = interval.start
        self.end = interval.end
        
    def __lt__(self, that):
        if self.start != that.start:
            return self.start < that.start
        else:
            return self.end < that.end

    def __str__(self):
        return str(self.start) + "-" + str(self.end)
        
class Solution:
    def employeeFreeTime(self, schedule: 'list<list<Interval>>') -> 'list<Interval>':
        heap = [] # [(start, end)]
        
        # Push all intervals into heap
        for row in schedule:
            for e in row:
                heappush(heap, HeapNode(e))
        
        if len(heap) < 1:
            return []
        
        node = heappop(heap)
        res = []
        while heap:
            top = heap[0]
            if node.end < top.start:
                # Case 1, found a new free slot
                res.append(Interval(node.end, top.start))
                node = heappop(heap)
            elif node.end < top.end:
                # Case 2, found a new node with later end time
                node = heappop(heap)
            else:
                # Case 3, current node all covers next node
                heappop(heap)
            
        return res
