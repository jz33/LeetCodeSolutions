'''
149. Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4

Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
'''
from collections import Counter
from decimal import *

INFINITE = 'infinite'

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0
        for p in points:
            samePoint = 0
            ctr = Counter()
            for q in points:
                x = q[0] - p[0]
                y = q[1] - p[1]
                if x == 0:
                    if y == 0:
                        samePoint += 1
                    else:
                        ctr[INFINITE] += 1
                else:
                    ctr[Decimal(y)/Decimal(x)] += 1
            res = max(res, samePoint + (ctr.most_common(1)[0][1] if ctr else 0))
        return res
