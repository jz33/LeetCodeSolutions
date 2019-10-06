'''
224. Basic Calculator
https://leetcode.com/problems/basic-calculator/

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2

Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
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
