'''
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        The maxium water on index i is the minimun of (highest height on its left
        and highest height on its right) - height on i
        '''
        size = len(height)
        leftHighests = [0] * size
        for i in range(1, size):
            leftHighests[i] = max(leftHighests[i-1], height[i-1])
            
        rightHighests = [0] * size
        for i in range(size-2, -1, -1):
            rightHighests[i] = max(rightHighests[i+1], height[i+1])
            
        res = 0
        for i in range(size):
            res += max(0, min(leftHighests[i], rightHighests[i]) - height[i])
        return res
