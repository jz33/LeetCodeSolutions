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
class Solution(object):
    def calculate(self, s):
        
        def comp(op: str, num: int):
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
        
        stack = []
        num = 0
        op = '+'
        for i in range(len(s)):
            if s[i].isdecimal():
                num = num * 10 + int(s[i])
                
            elif s[i] == '(':
                # Add to stack, will compute later in ')'
                stack.append(op)              
                num = 0
                op = '+'
                
            elif s[i] == ')':
                comp(op, num)
                
                num = 0
                while isinstance(stack[-1], int):
                    num += stack.pop()
                
                # Compute op before '('
                op = stack.pop()
                comp(op, num)
                
                num = 0
                
                # Set operator to nothing, so
                # next comp won't do anything
                op = ''
                
            elif s[i] in ['+', '-', '*', '/']:
                comp(op, num)
                num = 0
                op = s[i]
                
        comp(op, num) 
        return sum(stack)
