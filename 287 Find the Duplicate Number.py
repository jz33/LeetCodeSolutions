'''
287. Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist.
Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2

Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Use the idea of 142. Linked List Cycle II
        Because there is 1 duplcate, there must be a cycle
        '''
        slow = 0
        fast = 0
        maxLoopCount = len(nums) * 2

        for _ in range(maxLoopCount):
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break

        dupl = 0
        for _ in range(maxLoopCount):
            slow = nums[slow]
            dupl = nums[dupl]
            if slow == dupl:
                return dupl
            
        return -1
