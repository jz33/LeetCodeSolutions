'''
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

Constraints:
    1 <= n <= 8
'''
class Solution:
    '''
    The total number of answer is the Catalan number: (2n)! / (n+1)!n!
    Time complexity: O(4 ^ n / sqrt(n)), 
    Space complexity: O(n)
    https://leetcode.com/problems/generate-parentheses/editorial/
    '''
    def generateParenthesis(self, n: int) -> List[str]:
        pool = []

        def backtrack(sofar: List[str], left: int, right: int):
            if left == 0:
                pool.append(''.join(sofar + [')'] * right))
            else:
                backtrack(sofar + ['('], left - 1, right)
                if right > left:
                    backtrack(sofar + [')'], left, right - 1)
        
        backtrack([], n, n)
        return pool
