'''
986. Interval List Intersections
https://leetcode.com/problems/interval-list-intersections/

You are given two lists of closed intervals, firstList and secondList,
where firstList[i] = [starti, endi] and secondList[j] = [startj, endj].
Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are
either empty or represented as a closed interval.
For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Example 1:

Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []

Constraints:
    0 <= firstList.length, secondList.length <= 1000
    firstList.length + secondList.length >= 1
    0 <= starti < endi <= 109
    endi < starti+1
    0 <= startj < endj <= 109 
    endj < startj+1
'''
from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]: 
        i1 = 0
        i2 = 0
        result = [] # [[start , end]]
        while i1 < len(firstList) and i2 < len(secondList):
            int1 = firstList[i1]
            int2 = secondList[i2]

            # This question only considers the intersections. If no intersection, dump both intervals.
            intersection = [max(int1[0], int2[0]), min(int1[1], int2[1])]
            if intersection[0] <= intersection[1]:
                result.append(intersection)

            # Move based on end
            if int1[1] < int2[1]:
                i1 += 1
            elif int1[1] > int2[1]:
                i2 += 1
            else:
                i1 += 1
                i2 += 1
   
        return result
    

'''
Facebook real interview question: merge 2 interval list as union rather than intersections
https://www.1point3acres.com/bbs/thread-1038850-1-1.html
'''
def merge(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    i1 = 0
    i2 = 0
    int1 = None # Notice i1 or i2 are not necessarily in the list, they can be unioned interval too
    int2 = None
    result = [] # [[start , end]]
    while i1 < len(firstList) and i2 < len(secondList):
        if int1 is None:
            int1 = firstList[i1]
        if int2 is None:
            int2 = secondList[i2]

        intersection = [max(int1[0], int2[0]), min(int1[1], int2[1])]
        if intersection[0] > intersection[1]:
            # If no intersection, append the smaller one
            if int1[1] < int2[1]:
                result.append(int1)
                int1 = None
                i1 += 1
            else:
                result.append(int2)
                int2 = None
                i2 += 1
        else:
            # If intersection, hold the unioned interval
            if int1[1] < int2[1]:
                int2 = [min(int1[0], int2[0]), int2[1]]
                int1 = None
                i1 += 1
            else:
                int1 = [min(int1[0], int2[0]), int1[1]]
                int2 = None
                i2 += 1

    # Merge the remaining unioned interval
    if int1:
        result.append(int1)
        i1 += 1
    if int2:
        result.append(int2)
        i2 += 1

    # Merge any remaining intervals
    while i1 < len(firstList):
        result.append(firstList[i1])
        i1 += 1

    while i2 < len(secondList):
        result.append(secondList[i2])
        i2 += 1

    return result


testcases = [
    [
        [[1,2]],
        [[3,4]]
    ],
    [
        [[1,2], [3,5]],
        [[2,3]]
    ],
    [
        [[1,2], [3,5]],
        [[6,7], [9,11]]
    ],
    [
        [[1,2], [3,5], [7,9]],
        [[2,4], [5,10]]
    ],

]

for case in testcases:
    print(merge(case[0], case[1]))