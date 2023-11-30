'''
2158. Amount of New Area Painted Each Day
https://leetcode.com/problems/amount-of-new-area-painted-each-day/

There is a long and thin painting that can be represented by a number line.
You are given a 0-indexed 2D integer array paint of length n, where paint[i] = [starti, endi].
This means that on the ith day you need to paint the area between starti and endi.

Painting the same area multiple times will create an uneven painting so
you only want to paint each area of the painting at most once.

Return an integer array worklog of length n,
where worklog[i] is the amount of new area that you painted on the ith day.

Example 1:

Input: paint = [[1,4],[4,7],[5,8]]
Output: [3,3,1]
Explanation:
On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 4 and 7.
The amount of new area painted on day 1 is 7 - 4 = 3.
On day 2, paint everything between 7 and 8.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 8 - 7 = 1. 

Example 2:

Input: paint = [[1,4],[5,8],[4,7]]
Output: [3,3,1]
Explanation:
On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 5 and 8.
The amount of new area painted on day 1 is 8 - 5 = 3.
On day 2, paint everything between 4 and 5.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 5 - 4 = 1. 

Example 3:

Input: paint = [[1,5],[2,4]]
Output: [4,0]
Explanation:
On day 0, paint everything between 1 and 5.
The amount of new area painted on day 0 is 5 - 1 = 4.
On day 1, paint nothing because everything between 2 and 4 was already painted on day 0.
The amount of new area painted on day 1 is 0.

Constraints:
    1 <= paint.length <= 105
    paint[i].length == 2
    0 <= starti < endi <= 5 * 104
'''
from sortedcontainers import SortedDict

def getOverlap(aLeft: int, aRight: int, bLeft: int, bRight: int) -> int:
    return max(0, min(aRight, bRight) - max(aLeft, bLeft))

class Solution:
    def amountPainted(self, paints: List[List[int]]) -> List[int]:
        result = [0] * len(paints)
        ranges = SortedDict()  # {left: right}

        for ip, paint in enumerate(paints):
            totalOverlap = 0
            paintLeft, paintRight = paint

            # First, consider the nearest range on paintLeft.
            # If leftNearest has overlap on [paintLeft, paintRight], increase the overlap and shrink paintLeft
            # Below means get the range.left with range.left <= paintLeft
            leftNearest = next(ranges.irange(maximum=paintLeft, reverse=True), None)
            if leftNearest != None:
                leftNearestRight = ranges[leftNearest]
                overlap = getOverlap(
                    leftNearest, leftNearestRight, paintLeft, paintRight
                )
                if overlap > 0:
                    paintLeft = leftNearestRight
                    totalOverlap += overlap

            # Second, consider the nearest range on right.
            # If rightNearest has overlap on [paintLeft, paintRight], increase the overlap and shrink paintRight.
            # Notice after 1 check, paintLeft could >= paintRight.
            if paintLeft < paintRight:
                # Below means get the range.left with range.left < paintRight
                rightNearest = next(
                    ranges.irange(
                        maximum=paintRight, inclusive=(True, False), reverse=True
                    ),
                    None,
                )
                if rightNearest != None:
                    rightNearestRight = ranges[rightNearest]
                    # Unlike leftNearest, the rightNearest.right must >= paintRight. If not, treat it as between ranges.
                    if rightNearestRight > paintRight:
                        overlap = getOverlap(
                            paintLeft, paintRight, rightNearest, rightNearestRight
                        )
                        if overlap > 0:
                            paintRight = rightNearest
                            totalOverlap += overlap

            # Third, consider all ranges between paintLeft and paintRight.
            # These between ranges should not cross paintLeft or paintRight boundary.
            # Notice after above 2 checks, paintLeft could >= paintRight.
            if paintLeft < paintRight:
                # Notice left side should be inclusive
                # Convert to list as we want to iterate twice
                betweens = list(
                    ranges.irange(
                        minimum=paintLeft, maximum=paintRight, inclusive=(True, False)
                    )
                )
                for rangeLeft in betweens:
                    totalOverlap += getOverlap(
                        rangeLeft, ranges[rangeLeft], paintLeft, paintRight
                    )

                # Delete all between ranges
                for rangeLeft in betweens:
                    del ranges[rangeLeft]

                # Save the new range
                ranges[paintLeft] = paintRight

            result[ip] = paint[1] - paint[0] - totalOverlap
        return result
