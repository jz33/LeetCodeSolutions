'''
216. Combination Sum III
https://leetcode.com/problems/combination-sum-iii/

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
## Notice, the solution also requires each number only use once

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''
class Solution:
    def combinationSum3(self, count: int, target: int) -> List[List[int]]:
        candidates = [1,2,3,4,5,6,7,8,9]
        
        # The buf[t] is the list of all possible combination that sums to target
        buf = [[] for _ in range(target+1)]
        buf[0].append([])
    
        for c in candidates:
            for t in range(c, target+1):
                # Build buf[t] based on buf[t-c]
                for ls in buf[t-c]:
                    # Length check is the restriction of this problem
                    if len(ls) < count:
                        # Try to avoid using c more than once.
                        # If t-c < c, c is never used;
                        # Else, need to check if c is used
                        if t-c < c or c not in ls:
                            buf[t].append(ls + [c])

        return list(filter(lambda ls: len(ls) == count, buf[target]))
            
