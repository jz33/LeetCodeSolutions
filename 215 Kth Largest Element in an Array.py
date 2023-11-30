'''
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
    1 <= k <= nums.length <= 105
    -104 <= nums[i] <= 104
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        rank = k
        arr = nums
        while arr:
            pivot = random.choice(arr)
            smallers = [x for x in arr if x < pivot]
            middles = [x for x in arr if x == pivot] # Or just count the middle
            largers = [x for x in arr if x > pivot]

            if rank <= len(largers):
                # On the right larger array
                arr = largers
            elif rank > len(largers) + len(middles):
                # On the left smaller array
                arr = smallers
                rank = rank - len(largers) - len(middles)
            else:
                # In one of the middle section. They are all same, so just return the pivot
                return pivot
        return -1
