'''
632. Smallest Range Covering Elements from K Lists
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

You have k lists of sorted integers in ascending order.
Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:

Input: [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]

Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
'''
from heapq import heappush, heappop

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        '''
        Similar way to 23 Merge K Sorted List
        Use a heap to get min of all lists
        Manually update max
        '''
        heap = [] # (v, i, j)
        
        # Put first elements into heap
        for i in range(len(nums)):
            heappush(heap, (nums[i][0], i, 0))
        
        maxValue = max(row[0] for row in nums)
        
        # Answer
        left = -1e9
        right = 1e9
        
        while heap:
            v, i, j = heappop(heap) # v is min
            if right - left > maxValue - v:
                left = v
                right = maxValue
            
            if j + 1 == len(nums[i]):
                return [left, right]
            
            nv = nums[i][j+1]
            maxValue = max(maxValue, nv)
            heappush(heap, (nv, i, j+1))
            
        return [left, right]
