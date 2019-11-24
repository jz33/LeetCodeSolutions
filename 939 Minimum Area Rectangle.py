'''
939. Minimum Area Rectangle
https://leetcode.com/problems/minimum-area-rectangle/

Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points,
with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
'''
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        minArea = float('inf')
        
        # x : set(y)
        ref = collections.defaultdict(set)
        for a in points:
            ref[a[0]].add(a[1])
        
        for a in points:
            for b in points:
                if a[0] != b[0] and a[1] != b[1]:
    
                    # We need 4 points, a, b, (a[0], b[1]) and (b[0], a[1])
                    if b[1] in ref[a[0]] and a[1] in ref[b[0]]:
                        minArea = min(minArea, abs((a[0] - b[0]) * (a[1] - b[1])))

        return minArea if minArea != float('inf') else 0
