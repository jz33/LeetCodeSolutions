'''
442 Find All Duplicates in an Array
https://leetcode.com/problems/find-all-duplicates-in-an-array/

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums) + 1
        for e in nums:
            real_e = e % n
            nums[real_e - 1] += n # record e
        return [i for i in range(1,n) if nums[i-1] // n == 2]
