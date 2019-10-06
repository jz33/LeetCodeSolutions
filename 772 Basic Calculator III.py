'''
772. Basic Calculator III
https://leetcode.com/problems/basic-calculator-iii/

Implement a basic calculator to evaluate a simple expression string.
The expression string may contain open ( and closing parentheses ),
the plus + or minus sign -, non-negative integers and empty spaces .
The expression string contains only non-negative integers, +, -, *, / operators,
open ( and closing parentheses ) and empty spaces.
The integer division should truncate toward zero.

You may assume that the given expression is always valid.
All intermediate results will be in the range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
'''
class Solution:
    '''
    Stack, O(n)
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
