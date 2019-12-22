'''
84 Largest Rectangle in Histogram
https://leetcode.com/company/google/

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:        
        heights = [0] + heights + [0] # just to make code simpler
        stack = [0] # stack of indexes, where heights[i] are increasing
        maxRec = 0
        for i, h in enumerate(heights):
            while h < heights[stack[-1]]:
                j = stack.pop()
                recHeight = heights[j]
                # recHeight is the target rectangle's height, 
                # its right is before i, its left is after stack[-1], 
                # all heights between stack[-1] and j (even not in stack)
                # should be equal or larger than recHeight
                maxRec = max(maxRec, (i-1-stack[-1]) * recHeight)
            stack.append(i)
        return maxRec
