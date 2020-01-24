'''
77. Combinations
https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
class Solution:
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
