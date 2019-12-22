'''
932. Beautiful Array
https://leetcode.com/problems/beautiful-array/

For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:

For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].

Given N, return any beautiful array A.  (It is guaranteed that one exists.)

Example 1:

Input: 4
Output: [2,1,4,3]

Example 2:

Input: 5
Output: [3,1,2,5,4]
'''
class Solution:
    def rec(self, pairs):
        if len(pairs) == 1:
            return [pairs[0][0]]
        if len(pairs) == 2:
            return [pairs[0][0], pairs[1][0]]
            
        evens = []
        odds = []
        isOdd = True
        for ori, div in pairs:
            if isOdd:
                odds.append((ori, div >> 1))
            else:
                evens.append((ori, div >> 1))
            isOdd = not isOdd 
        
        return self.rec(evens) + self.rec(odds)
            
    def beautifulArray(self, N: int) -> List[int]:
        '''
        The idea is to put even numbers in first half,
        odd number in second half, then any pair from first half
        and second half their sum will be an odd number, which won't fit.
        Then do first and second half recursively
        '''
        r = range(1, N+1)
        return self.rec(list(zip(r, r)))
