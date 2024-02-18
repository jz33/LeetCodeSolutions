'''
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k,
return the k most frequent elements.
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
import random
from typing import List
from collections import Counter

class Solution1:
    '''
    Use sort O(nlogk)
    The return is sorted
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        histogram = Counter(nums)
        ls = sorted(histogram.items(), key = lambda x : -x[1])
        return [p[0] for p in ls[:k]]
    
from heapq import heappush, heappop
class Solution2:
    '''
    Use heap, O(nlogk)
    Should be fastest in reality, as heap is shallow
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        histogram = Counter(nums)

        heap = [] # min heap
        for key, count in histogram.items():
            heappush(heap, (count, key))
            if len(heap) > k:
                heappop(heap)
        
        # Just return the heap as order is not required
        return [pair[1] for pair in heap]

class Solution3:
    '''
    Use quick select, O(n)
    Works as the return order is not required
    Similar to 215. Kth Largest Element in an Array
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        histogram = Counter(nums)
        rank = k
        items = list(histogram.items()) # [(key, count)]
        result = []
        while items:
            pivot = random.choice(items)
            smalls = [pair for pair in items if pair[1] < pivot[1]]
            middles = [pair for pair in items if pair[1] == pivot[1]]
            larges = [pair for pair in items if pair[1] > pivot[1]]

            if rank <= len(larges):
                # On the right larger array
                items = larges
            elif rank > len(larges) + len(middles):
                # On the left smaller array
                items = smalls
                rank = rank - len(larges) - len(middles)
                result += middles + larges
            else:
                # In one of the middle section. Done
                result += larges + middles[:rank - len(larges)]
                break
            
        return [item[0] for item in result]
    
sol = Solution3()
print(sol.topKFrequent([1,1,1,2,2,3,3,4], 4))