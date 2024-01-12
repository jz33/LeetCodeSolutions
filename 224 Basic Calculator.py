'''
224. Basic Calculator
https://leetcode.com/problems/basic-calculator/

Given a string s representing a valid expression, implement a basic calculator to evaluate it,
and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
such as eval().

Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:

Input: s = " 2-1 + 2 "
Output: 3

Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Constraints:
    1 <= s.length <= 3 * 105
    s consists of digits, '+', '-', '(', ')', and ' '.
    s represents a valid expression.
    '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
    '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
    There will be no two consecutive operators in the input.
    Every number and running calculation will fit in a signed 32-bit integer.
'''
class Solution:
    '''
    This calculator needs to consider +, -, (, ), but not *, /
    Can re-use 772. Basic Calculator III, but can reduce stack size
    '''
    def calculate(self, s: str) -> int:
        stack = [0] # [operator or number]
        num = 0
        op = '+' # can be '+', '-' or None

        def compute():
            nonlocal stack, num, op
            # Directly compute +, -, no need to hold, as there is no *, /
            if op == '+':
                stack[-1] = stack[-1] + num
            elif op == '-':
                stack[-1] = stack[-1] - num

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in ['+', '-']:
                compute()
                op = c
                num = 0
            elif c == '(':
                # There must be an operator ahead of '('
                stack += [op, 0]
                op = '+'
                # number = 0 # Not needed as number is set to 0 on previous operator
            elif c == ')':
                compute()

                # The sum of the numbers inside parentheses must be stack[-1]
                num = stack.pop()
                op = stack.pop()
                compute()

                # As next char must be an operator,
                # set to None to avoid duplicate computing
                op = None 
                num = 0

        compute()
        return stack[-1]