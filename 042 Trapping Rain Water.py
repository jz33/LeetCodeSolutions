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
    '''
    Use Prefix Sum. This approach needs O(n) space
    '''
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

class Solution2:
    '''
    Two pointers approach, O(1) space
    '''
    def trap(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        leftHighest, rightHighest = 0, 0
        water = 0
        while left < right:
            if heights[left] < heights[right]:
                # Index left can possibly hold water as there is a higher right
                if heights[left] > leftHighest:
                    # Index left cannot hold water as it does not have a higher left
                    leftHighest = heights[left] 
                else:
                    # It must be leftHighest < rightHighest, as it only moves left when eights[left] < heights[right] 
                    water += leftHighest - heights[left]
                left += 1
            else: # heights[left] >= heights[right]
                if heights[right] > rightHighest:
                    rightHighest = heights[right]
                else:
                    water += rightHighest - heights[right]
                right -= 1

        # Eventually, left and right will meet in leftHighest or rightHighest
        return water

