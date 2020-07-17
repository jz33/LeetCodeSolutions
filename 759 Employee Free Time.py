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
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        heap = [] # [(start, end)], min heap
        for employee in schedule:
            for interval in employee:
                heappush(heap, (interval.start, interval.end))
        
        if not heap:
            return []
        
        node = heappop(heap)
        result = []
        while heap:
            top = heap[0]
            if node[1] < top[0]:
                # Case 1, an unoverlapped interval (a new free slot)
                result.append(Interval(node[1], top[0]))
                node = heappop(heap)
            elif node[1] < top[1]:
                # Case 2, next node with later end time
                node = heappop(heap)
            else:
                # Case 3, current node all covers next node
                heappop(heap)         
        return result
