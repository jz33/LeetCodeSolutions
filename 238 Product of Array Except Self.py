'''
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/submissions/

Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0:
            return []
        
        res = [1] * len(nums)
        
        # Reversed Symmetric  
        p = 1
        for i in range(1, len(nums)):
            p *= nums[i-1]
            res[i] *= p
                    
        p = 1
        for i in range(len(nums)-2,-1,-1):
            p *= nums[i+1]
            res[i] *= p
            
        return res
