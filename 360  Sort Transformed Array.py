'''
360. Sort Transformed Array
https://leetcode.com/problems/sort-transformed-array/

Given a sorted array of integers nums and integer values a, b and c.
Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]

Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
'''
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:     
        def compute(x):
            return a * x * x + b * x + c
        
        '''
        For quadratic function, the output curve is parabolic, that is,
        if a > 0 then center is smallest, if a < 0, center is biggest
        '''
        i = 0
        j = len(nums) - 1
        k = len(nums) - 1 if a >= 0 else 0
        res = [None] * len(nums)
        while i <= j:
            ci = compute(nums[i])
            cj = compute(nums[j])
            if a >= 0:
                # As sides are bigger, need biggest 
                if ci >= cj:
                    res[k] = ci
                    i += 1
                else:
                    res[k] = cj
                    j -= 1
                k -= 1
            else:
                # As sides are smaller, need smallest
                if ci <= cj:
                    res[k] = ci
                    i += 1
                else:
                    res[k] = cj
                    j -= 1
                k += 1
                
        return res
