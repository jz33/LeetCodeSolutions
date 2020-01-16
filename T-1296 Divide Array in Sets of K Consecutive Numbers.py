'''
1296. Divide Array in Sets of K Consecutive Numbers
https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

Given an array of integers nums and a positive integer k,
find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].

Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].

Example 3:

Input: nums = [3,3,2,2,1,1], k = 3
Output: true

Example 4:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.
'''
from heapq import heappush, heappop

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        '''
        Similar to 659. Split Array into Consecutive Subsequences
        '''
        if len(nums) % k != 0:
            return False
        
        # {ending num : [size subsequences ending with num]}
        book = collections.defaultdict(list)
        for n in sorted(nums):
            if len(book[n-2]) > 0 and book[n-2][0] < k:
                # No more chance to fill subsequence book[n-2][0]
                return False
            
            if len(book[n-1]) == 0:
                # No previous num
                heappush(book[n], 1)
            else:
                # Upgrade n-1 subsequence to n
                # Always fill shortest subsequence
                ctr = heappop(book[n-1]) + 1
                if ctr < k:
                    heappush(book[n], ctr)
        
        return all(len(ls) == 0 for ls in book.values())
