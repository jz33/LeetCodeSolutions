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
        stack = []
        maxArea = 0
        
        def compute(i, h):
            nonlocal stack, maxArea
            while stack and h < heights[stack[-1]]:
                j = stack.pop()
                recHeight = heights[j]
                
                # The rectangle width is from stack[-1] (exclusive) to i (exclusive)
                recWidth = i - 1 - stack[-1] if stack else i
                maxArea = max(maxArea, recHeight * recWidth)
        
        for i, h in enumerate(heights):
            compute(i, h)
            stack.append(i)
            
        compute(len(heights), 0)
        return maxArea
