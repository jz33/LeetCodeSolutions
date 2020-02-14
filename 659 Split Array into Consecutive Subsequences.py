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
        Build a dict to record subsequence lengths.
        Key is the max (right) number of a subsequence, value is list of
        subsequence sizes.
        '''
        book = collections.defaultdict(list)
        for n in nums:
            if len(book[n-2]) > 0 and book[n-2][0] < 3:
                return False
                    
            countList = book[n-1]
            if not countList:
                heappush(book[n], 1)
            else:
                # Use heap to always add to shorted subsequence first
                count = heappop(book[n-1]) + 1
                heappush(book[n], count)
        
        return all(count >= 3 for countList in book.values() for count in countList)    
