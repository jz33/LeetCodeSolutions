'''
224. Basic Calculator
https://leetcode.com/problems/basic-calculator/
227. Basic Calculator II
https://leetcode.com/problems/basic-calculator-ii/
772. Basic Calculator III
https://leetcode.com/problems/basic-calculator-iii/
'''
class Solution:
    '''
    Use exact same method for:
    224. Basic Calculator
    227. Basic Calculator II
    772. Basic Calculator III
    '''
    def compute(self, op, num, stack):
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            stack.append(stack.pop() * num)
        elif op == '/':
            # Notice how Python3 doing integer division on negative results
            last = stack.pop()
            if last // num < 0 and last % num != 0:
                stack.append(last // num + 1)
            else:
                stack.append(last // num)
                
    def collapse(self, stack):
        num = 0
        # Collpase on stack to compute the result inside brackets
        # No need to check if stack is null because there is a str op in front.
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
                op = '' # Let next char determine operator
                num = 0
        
        self.compute(op, num, stack)
        return sum(stack) 
