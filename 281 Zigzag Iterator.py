'''
281. Zigzag Iterator
https://leetcode.com/problems/zigzag-iterator/

Given two 1d vectors, implement an iterator to return their elements alternately.

Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6] 
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,3,2,4,5,6].
 

Follow up:

What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases.
If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].
'''
from heapq import heappush, heappop

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        '''
        Compute the complete output data.
        Similar to merge sorted lists.
        Easily extand to k vectors cases
        '''
        src = [v1, v2]
        data = []
        heap = [] # [(index in the array, the id of the array)]
        for arrId, arr in enumerate(src):
            if arr:
                heappush(heap, (0, arrId))
        
        while heap:
            index, arrId = heappop(heap)
            data.append(src[arrId][index])
            
            if index + 1 < len(src[arrId]):
                heappush(heap, (index + 1, arrId))
                
        self.data = data
        self.i = 0

    def next(self) -> int:
        r = self.data[self.i]
        self.i += 1
        return r
        
    def hasNext(self) -> bool:
        return self.i < len(self.data)
