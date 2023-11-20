/*
2158. Amount of New Area Painted Each Day
https://leetcode.com/problems/amount-of-new-area-painted-each-day/

There is a long and thin painting that can be represented by a number line.
You are given a 0-indexed 2D integer array paint of length n, where paint[i] = [starti, endi].
This means that on the ith day you need to paint the area between starti and endi.

Painting the same area multiple times will create an uneven painting so you only want to paint each area of the painting at most once.

Return an integer array worklog of length n, where worklog[i] is the amount of new area that you painted on the ith day.

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


*/
class Solution {
    public int getOverlap(int aLeft, int aRight, int bLeft, int bRight) {
        return Math.max(0, Math.min(aRight, bRight) - Math.max(aLeft, bLeft));
    }

    public int[] amountPainted(int[][] paint) {
        var result = new int[paint.length];

        // Use TreeMap to track intervals (aka ranges), similary to 715. Range Module
        // The map only contains non-overlapped ranges.
        var rangesMap = new TreeMap<Integer, Integer>(); // { start : end }

        for (int i = 0; i < paint.length; i++) {
            var range = paint[i];
            var left = range[0];
            var right = range[1];
            var totalOverlap = 0; // total overlap to remove on i

            // First, consider the nearest range on left.
            // If leftNearest has overlap on [left, right], increase the overlap and shrink left bound
            var leftNearest = rangesMap.floorEntry(left);
            if (leftNearest != null) {
                var overlap = getOverlap(leftNearest.getKey(), leftNearest.getValue(), left, right);
                if (overlap > 0) {
                    left = leftNearest.getValue();
                }
                totalOverlap += overlap;
            }
            // Second, consider the nearest range on right.
            // If rightNearest has overlap on [left, right], increase the overlap and shrink right bound.
            // However, unlike leftNearest, the rightNearest's right bound must > right. If not, treat it 
            // as between ranges.
            // Notice after 1 check, left could > right.
            if (left < right) {
                var rightNearest = rangesMap.lowerEntry(right);
                if (rightNearest != null) {
                    if (rightNearest.getValue() > right) {
                        var overlap = getOverlap(rightNearest.getKey(), rightNearest.getValue(), left, right);
                        if (overlap > 0) {
                            right = rightNearest.getKey();
                        }
                        totalOverlap += overlap;
                    }
                }
            }
            // Third, consider all ranges between left and right.
            // These between ranges should not cross left or right boundary.
            // Notice after above 2 checks, left could > right.
            if (left < right ) {
                var betweens = rangesMap.subMap(left, true, right, false);
                for (var entry : betweens.entrySet()) {
                    totalOverlap += getOverlap(entry.getKey(), entry.getValue(), left, right);
                }
                betweens.clear();
                rangesMap.put(left, right);
            }
            // Save result
            result[i] = range[1] - range[0] - totalOverlap;
        }
        return result;
    }
}
