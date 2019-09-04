'''
Top K Frequent Elements 
https://leetcode.com/problems/top-k-frequent-elements/
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        A strict O(n) method without sort
        '''
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

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        An O(nlog(n)) method with sort
        '''
        # 1. Build histogram
        histogram = {}
        for n in nums:
            histogram[n] = histogram.get(n,0) + 1
        
        # 2. Sort
        ls = sorted(histogram.items(), key = lambda x : -x[1])
        
        # 3. Slice
        return [p[0] for p in ls[:k]]
