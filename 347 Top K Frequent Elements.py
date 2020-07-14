'''
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
'''

### 1. A strict O(n) method without sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Build histogram and find maximun frequency
        histogram = {}
        maxFreq = 0
        for n in nums:
            freq = histogram.get(n,0) + 1
            maxFreq = max(maxFreq,freq)
            histogram[n] = freq
        
        # 2. Build reversed histogram
        revHisto = {}
        for key, val in histogram.items():
            revHisto[val] = revHisto.get(val,[]) + [key]
        
        # 3. Count from maximun frequency
        res = []
        while len(res) < k:
            res.extend(revHisto.get(maxFreq,[]))
            maxFreq -= 1
        return res[:k]


### 2. An O(nlog(n)) method with sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Build histogram
        histogram = collections.Counter(nums)

        # 2. Sort
        ls = sorted(histogram.items(), key = lambda x : -x[1])
        
        # 3. Slice
        return [p[0] for p in ls[:k]]
    
    
### 3. Use Heap
from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)

        heap = [] # min heap
        for key, ctr in counter.items():
            heappush(heap, (ctr, key))
            if len(heap) > k:
                heappop(heap)
        
        res = []
        while heap:
            res.append(heappop(heap)[1])
        return res[::-1]
