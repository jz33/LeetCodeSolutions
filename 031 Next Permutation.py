'''
31. Next Permutation
https://leetcode.com/problems/next-permutation/

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples.
Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if not nums or not len(nums):
            return
        
        # From back, find first number who is smaller than its next number
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                break
        else:
            # If not found, set i to -1 for reverse
            i = -1
            
        # Reverse all the numbers after i
        nums[i+1:] = nums[i+1:][::-1]
        
        # If i is not found, we have converted from last permutation to first one.
        # e.g, [3,2,1] => [1,2,3]. Done
        if i == -1:
            return
        
        # Find first number after i that is larger than nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                break
                
        # Swap nums[i], nums[j]. Done
        nums[i], nums[j] = nums[j], nums[i]
