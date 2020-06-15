'''
692. Top K Frequent Words
https://leetcode.com/problems/top-k-frequent-words/

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, 
then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
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

from heapq import heappush, heappop
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        Use heap
        '''
        counter = Counter(words)

        heap = [] # min heap
        for key, ctr in counter.items():
            heappush(heap, (ctr, key))
            if len(heap) > k:
                heappop(heap)
        
        res = []
        while heap:
            res.append(heappop(heap)[1])
        return res[::-1]
