'''
556. Next Greater Element III
https://leetcode.com/problems/next-greater-element-iii/

Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which
has exactly the same digits existing in the integer n and is greater in value than n.
If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21

Example 2:

Input: 21
Output: -1
'''
MAX_SINGED_INT32 = 2 ** 31 - 1

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        '''
        Solution based on 31 Next Permutation
        '''
        nums = list(str(n))
        if len(nums) < 2:
            return -1
        
        # 1. From back, find first number who is smaller than its next number
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                break
        else:
            # Not found
            return -1
            
        # 2. Reverse all the numbers after i
        nums[i+1:] = nums[i+1:][::-1]
        
        # 3. Find first number after i that is larger than nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                break
                
        # 4. Swap nums[i], nums[j]. Done
        nums[i], nums[j] = nums[j], nums[i]
        
        res = int(''.join(nums))
        
        # If result is bigger than biggest signed 32-bit integer, return -1
        return res if res <= MAX_SINGED_INT32 else -1
