'''
640. Solve the Equation
https://leetcode.com/problems/solve-the-equation/

Solve a given equation and return the value of x in the form of string "x=#value".
The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".
If there are infinite solutions for the equation, return "Infinite solutions".
If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"

Example 2:
Input: "x=x"
Output: "Infinite solutions"

Example 3:
Input: "2x=x"
Output: "x=0"

Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"

Example 5:
Input: "x=x+2"
Output: "No solution"
'''
class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=', 1)
        leftX, leftNum = self.evaluate(left)
        rightX, rightNum = self.evaluate(right)
        
        paramX = leftX - rightX
        paramNum = rightNum - leftNum
        if paramX == 0 and paramNum == 0:
            return "Infinite solutions"
        if paramX == 0:
            return "No solution"
        return "x=" + str(paramNum // paramX)
    
    def evaluate(self, expr: str):
        rx, rn = 0, 0 # result
        num = None # number
        sign = 1 # sign
        hasX = False # if there is an X
        
        def compute():
            nonlocal rx, rn, num, sign, hasX
            if hasX:
                if num is None: # Consider 0x case
                    num = 1
                rx += num * sign
            elif num:
                rn += num * sign
            
            num = None
            hasX = False
        
        for e in expr:
            if e == 'x':
                hasX = True
            elif e == '+':
                compute()
                sign = 1
            elif e == '-':
                compute()
                sign = -1
            else: # digit
                if not num: # num == 0 or num == None
                    num = int(e)
                else:
                    num = num * 10 + int(e)
        compute()
        return rx , rn
