'''
31. Next Permutation
https://leetcode.com/problems/next-permutation/

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr:
[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order,
then the next permutation of that array is the permutation that follows it in the sorted container.
If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

    For example, the next permutation of arr = [1,2,3] is [1,3,2].
    Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
    While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 100
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return
   
        # From right find pivot, aka, the first number who is smaller than its right neighbor.
        pivot = None
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break

        if pivot is None:
            # All elements of nums are in descending order,
            # aka, nums is in its last permutation state.
            # Reverse all and return
            nums[:] = nums[::-1]
            return

        # Reverse all the numbers after pivot,
        # because elements in nums[pivot+1:] are in descending order,
        # aka, nums[pivot+1:] is in its last permutation.
        # After reverse, nums[pivot+1:] is in ascending order
        nums[pivot+1:] = nums[pivot+1:][::-1]

        # Find first number after pivot that is larger than nums[pivot]
        bigger = pivot
        for i in range(pivot+1, len(nums)):
            if nums[i] > nums[pivot]:
                bigger = i
                break

        # The bigger number must exist, as last permutation case is filtered before.
        # Swap. Done
        nums[pivot], nums[bigger] = nums[bigger], nums[pivot]
