'''
84 Largest Rectangle in Histogram
https://leetcode.com/company/google/
http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:        
        heights = [0] + heights + [0] # just to make code simpler
        stack = [0] # record indexes, where heights are increasing
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
