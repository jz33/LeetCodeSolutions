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
        res = [0, float('inf')]
        
        heap = [] # [(value, arr index i, arr[i] index)]
        for i, arr in enumerate(nums):
            if arr:
                heappush(heap, (arr[0], i, 0))
        
        maxVal = max(t[0] for t in heap)
        
        # The result interval is the min/max value of the heap
        while heap:
            minVal, i, j = heappop(heap)
   
            if maxVal - minVal < res[1] - res[0]:          
                res = [minVal, maxVal]
            
            if j + 1 == len(nums[i]):
                return res
            
            nextVal = nums[i][j+1]
            maxVal = max(maxVal, nextVal)                
            
            heappush(heap, (nextVal, i, j+1))
            
        return res
