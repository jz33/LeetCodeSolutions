'''
503. Next Greater Element II
https://leetcode.com/problems/next-greater-element-iii/

Given a circular array (the next element of the last element is the first element of the array),
print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to
its traversing-order next in the array, which means you could search circularly to find its next greater number.
If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;

The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
'''
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # Find last greatest element
        maxNum, maxIndex = None, None
        for i, e in enumerate(nums):
            if maxNum is None or e >= maxNum:
                maxNum, maxIndex = e, i
                
        # Use monotonic stack to scan elements [maxIndex + 1:], [:maxIndex + 1]
        # Similar to 739 Daily Temperatures
        res = [-1] * len(nums)
        stack = [] # indexes

        for i in range(maxIndex + 1, len(nums)):
            val = nums[i]
            while stack and val > nums[stack[-1]]:
                last = stack.pop()
                res[last] = val
            if val != maxNum:
                stack.append(i)
        
        for i in range(maxIndex + 1):
            val = nums[i]
            while stack and val > nums[stack[-1]]:
                last = stack.pop()
                res[last] = val
            if val != maxNum:
                stack.append(i)
        
        return res
