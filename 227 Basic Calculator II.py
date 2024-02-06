'''
227. Basic Calculator
https://leetcode.com/problems/basic-calculator-ii/

Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid.
All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,such as eval().

Example 1:

Input: s = "3+2*2"
Output: 7

Example 2:

Input: s = " 3/2 "
Output: 1

Example 3:

Input: s = " 3+5 / 2 "
Output: 5

Constraints:
    1 <= s.length <= 3 * 105
    s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
    s represents a valid expression.
    All the integers in the expression are non-negative integers in the range [0, 231 - 1].
    The answer is guaranteed to fit in a 32-bit integer.
'''
class Solution:
    '''
    This calculator needs to consider +, -, *, /, but not parentheses
    Can re-use 772. Basic Calculator III, but using stack is inefficient, should do extra memory in O(1)
    '''
    def calculate(self, s: str) -> int:
        result = 0
        # When encounters a delimiter ('+', '-', '*', '/' or EOF), currNum is the number before the delimiter,
        # op is the operator before currNum, prevNum is the number before operator
        # For example: 1 - 2 * 3, if reaches '*', prevNum = 1, currNum = 2, op = '-'
        op = '+'
        prevNum = 0
        currNum = 0

        def compute():
            nonlocal result, op, prevNum, currNum
            if op == '+':
                # This cannot be prevNum = prevNum + currNum, as next operator could be *, /
                result += prevNum
                prevNum = currNum
            elif op == '-':
                result += prevNum
                prevNum = -currNum
            elif op == '*':
                prevNum = prevNum * currNum
            elif op == '/':
                if prevNum // currNum < 0 and prevNum % currNum != 0:
                    prevNum = prevNum // currNum + 1
                else:
                    prevNum = prevNum // currNum

        for c in s:
            if c.isdecimal():
                currNum = currNum * 10 + int(c)   

            elif c in ['+', '-', '*', '/']:
                # compute when at delimiter or at the end of line
                compute()
                op = c
                currNum = 0
                
        compute()
        return result + prevNum
    
'''
Real Facebook Interview: only consider number and '+'
https://www.1point3acres.com/bbs/thread-1043252-1-1.html
'''
class Solution2:
    def calculate(self, s: str) -> int:
        result = 0
        currNum = 0
        for c in s:
            if c == '+':
                result += currNum
                currNum = 0
            elif c.isdecimal():
                currNum = currNum * 10 + int(c)    
        return result + currNum
    

sol = Solution2()
formula = [
    '1+3',
    '2',
    '7+2',
    '1+1+1+5',
]
for f in formula:
    print('{0} equals {1}'.format(f, sol.calculate(f)))
