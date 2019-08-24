'''
22 Generate Parentheses
https://oj.leetcode.com/problems/generate-parentheses/
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pool = []
        
        def backtrack(ss: List[str], left:int, right:int):
            if len(ss) == 2 * n:
                pool.append(''.join(ss))
                return;

            if left < n:
                ss.append('(')
                backtrack(ss, left + 1, right)
                ss.pop() # this is why this is called "backtrack"

            if right < left:
                ss.append(')')
                backtrack(ss, left, right + 1)
                ss.pop()
                
        backtrack([], 0, 0)
        return pool
