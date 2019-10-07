'''
986. Interval List Intersections
https://leetcode.com/problems/interval-list-intersections/

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that is either empty,
or can be represented as a closed interval.
For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:

Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
'''
class Solution:
    def compare(self, a: List[int], b: List[int])-> int:
        '''
        Compare 2 intervals
        '''
        return a[1] - b[1]
    
    def getIntersection(self, a: List[int], b: List[int]) -> List[int]:
        '''
        Get intersection interval of 2 intervals
        '''
        left = max(a[0], b[0])
        right = min(a[1], b[1])
        
        if left <= right:
            return [left, right]
        else:
            return None
    
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            a = A[i]
            b = B[j]
            intersection = self.getIntersection(a, b)
            if intersection is not None:
                res.append(intersection)

            # The interval who ends earlier can be dumped
            comp = self.compare(a, b)
            if comp == 0:
                i += 1
                j += 1
            elif comp < 0:
                i += 1
            else:
                j += 1

        return res
