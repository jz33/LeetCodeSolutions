'''
57. Insert Interval
https://leetcode.com/problems/insert-interval/

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]

Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''
class Solution:
    def getInsertionPoint(self, intervals, target) -> int:
        left = 0
        right = len(intervals) - 1
        while left <= right:
            mid = left + (right - left) // 2
            midStart = intervals[mid][0]
            if midStart == target:
                return mid
            elif midStart < target:
                left = mid + 1
            else:
                right = mid - 1
        return -left

    def getLeftBoundary(self, intervals, newInterval):
        i = self.getInsertionPoint(intervals, newInterval[0])
        if i >= 0:
            return i, newInterval[0]
        else:
            i = -i
            prev = intervals[i-1]
            if newInterval[0] <= prev[1]:
                # Overlapped
                return i-1, prev[0]
            else:
                return i, newInterval[0]

    def getRightBoundary(self, intervals, newInterval):
        i = self.getInsertionPoint(intervals, newInterval[1])
        if i == 0:
            if newInterval[1] < intervals[0][0]:
                return -1, newInterval[1]
            else:
                return 0, intervals[0][1]
        elif i > 0:
            return i, intervals[i][1]
        else:
            i = -i
            return i - 1, max(intervals[i-1][1], newInterval[1])

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        @intervals: sorted by starting index
        '''
        if not intervals:
            return [newInterval]

        # Get left/right exclusive boundries, and a new merged interval
        lb, li = self.getLeftBoundary(intervals, newInterval)
        rb, ri = self.getRightBoundary(intervals, newInterval)

        res = []
        for i in range(lb):
            res.append(intervals[i])

        res.append([li,ri])

        for i in range(rb+1, len(intervals)):
            res.append(intervals[i])
            
        return res
