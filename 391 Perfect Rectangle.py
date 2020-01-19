'''
391. Perfect Rectangle
https://leetcode.com/problems/perfect-rectangle/

Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point.
For example, a unit square is represented as [1,1,2,2].
(coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).

Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.
 
Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions. 

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
'''
def rectArea(rect: List[int]) -> int:
    return (rect[2] - rect[0]) * (rect[3] - rect[1])
    
def pointHash(x, y) -> str:
    return str(x) + '|' + str(y)
    
def isRectangleCover(rectangles: List[List[int]]) -> bool:
    left = min(rect[0] for rect in rectangles)
    bottom = min(rect[1] for rect in rectangles)
    right = max(rect[2] for rect in rectangles)
    top = max(rect[3] for rect in rectangles)
    totalArea = rectArea([left, bottom, right, top])

    points = collections.Counter()
    subAreas = 0
    for rect in rectangles:
        points[pointHash(rect[0], rect[1])] += 1
        points[pointHash(rect[0], rect[3])] += 1
        points[pointHash(rect[2], rect[1])] += 1
        points[pointHash(rect[2], rect[3])] += 1
        subAreas += rectArea(rect)

    # Check area. Should equal as rectangles should not overlap.
    if not totalArea == subAreas:
        return False

    # Check points
    corners = [pointHash(left, bottom), pointHash(left, top), pointHash(right, bottom), pointHash(right, top)]
    
    for point, ctr in points.items():
        if point in corners:
            if ctr != 1:
                return False
        else:
            if (ctr & 1) != 0:
                return False

    return True
    
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        return isRectangleCover(rectangles)
