'''
659. Split Array into Consecutive Subsequences
https://leetcode.com/problems/split-array-into-consecutive-subsequences/

Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences
such that each subsequence consists of consecutive integers and has length at least 3.

Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

Example 3:

Input: [1,2,3,4,4,5]
Output: False

'''
from heapq import heappush, heappop

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        '''
        Build a dict to record subsequences.
        Key is the max number of a subseq, value is list of
        subseq sizes, using heap to return shortest subseq
        '''
        book = collections.defaultdict(list)
        for n in nums:
            if n-1 not in book or len(book[n-1]) == 0:
                heappush(book[n], 1)
            else:
                ctr = heappop(book[n-1]) + 1
                heappush(book[n], ctr)
                    
        for k, ls in book.items():
            if any(ctr < 3 for ctr in ls):
                return False
            
        return True
        
