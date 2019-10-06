'''
282. Expression Add Operators
https://leetcode.com/problems/expression-add-operators/

Given a string that contains only digits 0-9 and a target value, return all possibilities
to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 

Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]

Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]

Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]

Example 5:

Input: num = "3456237490", target = 9191
Output: []
'''

class Solution:
    def dfs(self, i: int, expr: List[str], val: int, productVal: int):
        '''
        @i: current index in self.num
        @expr: current expression
        @val: value of current expression
        @productVal: the value of last product. Notice if last operator is not '*',
            treat it like 1/-1 * last value
        '''
        num = self.num
        if i == len(num):
            if val == self.target:
                self.pool.append(''.join(expr))
            return
        
        for j in range(i+1, len(num)+1):
            # Get each integer from num[i:]
            n = int(num[i:j])
            s = str(n)
            
            if len(s) < j - i:
                # '01', integer will be 1, and then interger string
                # is '1', which should break, because all later j
                # will have same issue
                break
            
            if i == 0:
                # Cannot put operator in beginning!
                self.dfs(j, expr + [s], n, n)
            else:
                self.dfs(j, expr + ['+', s], val + n, n)
                self.dfs(j, expr + ['-', s], val - n, -n)

                # productVal * n is the new product value, and old one (productVal) should be removed
                self.dfs(j, expr + ['*', s], val - productVal + productVal * n, productVal * n)
    
    def addOperators(self, num: str, target: int) -> List[str]:
        self.num = num
        self.target = target
        self.pool = []
        
        self.dfs(0, [], 0, 0)
        return self.pool
