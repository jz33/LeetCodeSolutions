'''
227. Basic Calculator II
https://leetcode.com/problems/basic-calculator-ii/

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces.
The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''
class Solution:
    '''
    Same like 772. Basic Calculator III
    '''
    def comp(self, op: str, num: int, stack):
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            stack.append(stack.pop() * num)
        elif op == '/':
            last = stack.pop()
            if last // num < 0 and last % num != 0:
                stack.append(last // num + 1)
            else:
                stack.append(last // num)
    
    def calculate(self, s: str) -> int:
        stack = []
        op = '+'
        num = 0
        for c in s:
            if c.isdecimal():
                num = num * 10 + int(c)
            elif c == '(':
                stack.append(op)
                num = 0
                op = '+'
            elif c == ')':
                self.comp(op, num, stack)
                
                # Compute everything between '(' and ')'
                num = 0
                while isinstance(stack[-1], int):
                    num += stack.pop()
                op = stack.pop()
                self.comp(op, num, stack)
                
                # Set op to nothing, as next char of ')'
                # will be an operator, which should not pre-do anything
                num = 0
                op = ''
            elif c in ['+', '-', '*', '/']:
                self.comp(op, num, stack)
                num = 0
                op = c
        
        self.comp(op, num, stack)
        return sum(stack)
