'''
41. First Missing Positive
https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
	
Example 2:

Input: [3,4,-1,1]
Output: 2
	
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # Swap a postive into its right place, for example, 3 should be put into index 2
            # Do this in while loop, because nums[nums[i]-1] might need to be swapped too.
            # This runs in O(n) as each number is swapped at most once
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            
        # Check from beginning
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        
        return len(nums) + 1
