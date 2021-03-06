'''
692. Top K Frequent Words
https://leetcode.com/problems/top-k-frequent-words/

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical order comes first.

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
from heapq import heappush, heappop

class HeapNode:
    def __init__(self, word: str, count: int):
        self.word = word
        self.count = count
        
    def __lt__(self, that):
        if self.count != that.count:
            return self.count < that.count
        
        # Think why...
        return self.word > that.word
        
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        
        heap = [] # [HeapNode], min heap
        for word, count in counter.items():
            heappush(heap, HeapNode(word, count))
            if len(heap) > k:
                heappop(heap)
    
        res = []
        while heap:
            res.append(heappop(heap).word)
        return res[::-1]
