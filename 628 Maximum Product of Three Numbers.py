'''
628. Maximum Product of Three Numbers
https://leetcode.com/problems/maximum-product-of-three-numbers/

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 

Example 2:

Input: [1,2,3,4]
Output: 24
'''
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        '''
        The result is either max 3 nums' product, or the max number 
        times top 2 min numbers.
        '''
        mins = [float('inf'), float('inf')] # mins[0] is smallest
        maxs = [float('-inf'), float('-inf'), float('-inf')] # max[0] is biggest
        for n in nums:
            if n < mins[0]:
                mins = [n, mins[0]]
            elif n < mins[1]:
                mins[1] = n
                
            if n > maxs[0]:
                maxs = [n, maxs[0], maxs[1]]
            elif n > maxs[1]:
                maxs = [maxs[0], n, maxs[1]]
            elif n > maxs[2]:
                maxs[2] = n
                
        return max(maxs[0] * maxs[1] * maxs[2], maxs[0] * mins[0] * mins[1])
