'''
77. Combinations
https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

Constraints:
    1 <= n <= 20
    1 <= k <= n
'''
class Solution:
    '''
    Recursive, backtrack
    Unlike permutation, elements not swapped, but added, as previous elements cannot be reused
    '''
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        # Establish the array for a general C(N, K) combination calculation
        nums = list(range(1, n+1, 1))
                   
        def backtrack(arr: List[int], start: int):
            if len(arr) == k:
                # deepcopy
                result.append(arr[:])
            else:
                for i in range(start, len(nums)):
                    arr.append(nums[i])
                    backtrack(arr, i + 1)
                    arr.pop()
                    
        backtrack([], 0)
        return result

class Solution:
    '''
    Iterative
    '''
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs, newCombs = [[]], []   
        for i in range(k):
            for row in combs:
                # The last number in previous result
                lastBit = row[-1] if len(row) > 0 else 0
                
                # Clearly, j needs to be start from next bit of lastBit.
                # What's the upper bound? 
                # The remaining available bits need to fit the result to k size
                # array, then there is this equation:
                # n - max_j >= k - (i + 1)
                # Left side is how many remaining bits, right side is how
                # many bits still needed.
                for j in range(lastBit + 1, n + 2 - k + i):
                    newCombs.append(row + [j])
                    
            combs, newCombs = newCombs, []       
        return combs
