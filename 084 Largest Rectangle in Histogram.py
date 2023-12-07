'''
84 Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/

Given an array of integers heights representing the histogram's bar height
where the width of each bar is 1,
return the area of the largest rectangle in the histogram.

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:

Input: heights = [2,4]
Output: 4

Constraints:
    1 <= heights.length <= 105
    0 <= heights[i] <= 104
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [decreasing indexes of heights]
        maxArea = 0
        
        def compute(i, h):
            nonlocal stack, maxArea
            # Compute previous rectangle size if height decreased on i,
            # as i cannot build a rectange with previous indexes
            while stack and h < heights[stack[-1]]:
                last = stack.pop()
                recHeight = heights[last]
                # The rectangle width is from stack[-1] (exclusive) to i (exclusive)
                recWidth = i - 1 - stack[-1] if stack else i
                maxArea = max(maxArea, recHeight * recWidth)
        
        for i, h in enumerate(heights):
            compute(i, h)
            stack.append(i)
            
        compute(len(heights), 0)
        return maxArea
