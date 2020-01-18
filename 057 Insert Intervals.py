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
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        # left and right boundary for overlapped interval
        left, right = newInterval[0], newInterval[1] 
        
        for it in intervals:
            if it[1] < newInterval[0]:
                # 1. Non-overlapping, it is in left branch
                res.append(it)
            elif it[0] > newInterval[1]:
                # 2. Non-overlapping, it is in right branch
                # Need to append the overlapped interval
                if left is not None:
                    res.append([left, right])
                    left = None # indicates overlapped interval is inserted
                res.append(it)
            else:
                # 3. Overlapping now. Update boundaries
                left = min(left, it[0])
                right = max(right, it[1])
        
        if left is not None:
            res.append([left, right])
            
        return res
