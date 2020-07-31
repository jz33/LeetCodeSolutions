'''
772. Basic Calculator III
https://leetcode.com/problems/basic-calculator-iii/
'''
'''
Same solution for
224. Basic Calculator
227. Basic Calculator II
772. Basic Calculator III
'''
class Solution:
    def compute(self, op: str, num: int, stack: List[int]):
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            stack.append(stack.pop() * num)
        elif op == '/':
            # Notice how Python3 doing integer division on negative input
            last = stack.pop()
            if last // num < 0 and last % num != 0:
                stack.append(last // num + 1)
            else:
                stack.append(last // num)
                
    def collapse(self, stack: List[int]):
        # Collapse on stack to compute the result inside bracket pair.
        # No need to check if stack is null because
        # there must be a string operator in front.
        num = 0
        while isinstance(stack[-1], int):
            num += stack.pop()
        op = stack.pop()
        self.compute(op, num, stack)
              
    def calculate(self, s: str) -> int:
        op = '+'
        num = 0
        stack = []
        for c in s:
            if c.isdecimal():
                num = num * 10 + int(c)              
            elif c in ['+', '-', '*', '/']:
                self.compute(op, num, stack)
                op = c
                num = 0
            elif c == '(':
                stack.append(op)
                op = '+'
                num = 0
            elif c == ')':
                self.compute(op, num, stack)
                self.collapse(stack)
                # No need to reset operator, let next char determine
                num = 0
        
        self.compute(op, num, stack)
        return sum(stack)
