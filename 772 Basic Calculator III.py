'''
772. Basic Calculator III
https://leetcode.com/problems/basic-calculator-iii/

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, '+', '-', '*', '/' operators,
and open '(' and closing parentheses ')'.
The integer division should truncate toward zero.

You may assume that the given expression is always valid.
All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "1+1"
Output: 2

Example 2:

Input: s = "6-4/2"
Output: 4

Example 3:

Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21

Constraints:
    1 <= s <= 104
    s consists of digits, '+', '-', '*', '/', '(', and ')'.
    s is a valid expression.
'''
class Solution:
    def calculate(self, s: str) -> int:
        stack = [] # [operator or number]
        number = 0
        operator = '+' # can be '+', '-', '*', '/',  or None

        # Compute whenever number parsing is done. 3 possibilities:
        # 1. Meet an operator
        # 2. Meet ')'
        # 3. End of s.
        def compute():
            nonlocal stack, number, operator
            if operator == '+':
                stack.append(number)
            elif operator == '-':
                stack.append(-number)
            elif operator == '*':
                stack[-1] = stack[-1] * number
            elif operator == '/':
                result = stack[-1] // number
                if result < 0 and stack[-1] % number != 0:
                    # This question asked to truncate toward zero
                    result += 1 
                stack[-1] = result
            # operator can be None too after parsing ')'
            
        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            elif c in ['+', '-', '*', '/']:
                compute()
                operator = c
                number = 0
            elif c == '(':
                # There must be an operator ahead of '('
                stack.append(operator)
                operator = '+'
                # number = 0 # Not needed as number is set to 0 on previous operator
            elif c == ')':
                compute()

                # Get sum of the numbers inside parentheses,
                # compute with the operator in front of '('
                number = 0
                while isinstance(stack[-1], int):
                    number += stack.pop()
                operator = stack.pop()
                compute()

                # As next char must be an operator,
                # set to None to avoid duplicate computing
                operator = None 
                number = 0

        compute()
        return sum(stack)
