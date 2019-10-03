'''
238. Product of Array Except Self
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if not size:
            return []
        
        res = [1] * size
        
        # 1. Let res[i] be the product of nums[:i]
        for i in range(1,size):
            res[i] = res[i-1] * nums[i-1]
                
        # 2. Then, res[-1] is already the answer
        # From right to left, res[i] = res[i] * right,
        # where right is product of nums[i+1:]
        right = 1
        for i in range(size-1, -1 ,-1):
            res[i] = res[i] * right
            right *= nums[i]
                
        return res
