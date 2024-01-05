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
    '''
    O(n) with quick select
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        rank = k
        arr = nums
        while arr:
            pivot = random.choice(arr)
            smalls = [x for x in arr if x < pivot]
            middles = sum(1 for x in arr if x == pivot)
            larges = [x for x in arr if x > pivot]

            if rank <= len(larges):
                # On the right larger array
                arr = larges
            elif rank > len(larges) + middles:
                # On the left smaller array
                arr = smalls
                rank = rank - len(larges) - middles
            else:
                # In one of the middle section. They are all same, so just return the pivot
                return pivot
        return -1

from heapq import heappush, heappop
class Solution:
    '''
    Use heap, O(nlogk)
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [] # min heap
        for n in nums:
            heappush(heap, n)
            if len(heap) > k:
                heappop(heap)
        return heap[0]