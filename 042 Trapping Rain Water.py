'''
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        The maximum water on index i is the minimum of (highest height on its left
        and highest height on its right) - height on i
        '''
        leftHighs = [0] * len(height) # leftHighs[i] is the highest in [:i]
        for i in range(1, len(height)):
            leftHighs[i] = max(leftHighs[i-1], height[i-1])
            
        rightHighs = [0] * len(height) # rightHighs[i] is the highest in [i+1:]
        for i in range(len(height)-2, -1, -1):
            rightHighs[i] = max(rightHighs[i+1], height[i+1])
            
        result = 0
        for i in range(len(height)):
            result += max(0, min(leftHighs[i], rightHighs[i]) - height[i])
        return result
