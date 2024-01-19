'''
282. Expression Add Operators
https://leetcode.com/problems/expression-add-operators/

Given a string num that contains only digits and an integer target,
return all possibilities to insert the binary operators '+', '-', and/or '*'
between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.

Example 3:

Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.

Constraints:
    1 <= num.length <= 10
    num consists of only digits.
    -231 <= target <= 231 - 1
'''
class Solution:
    '''
    Complexity: O (3 ^ N)
    Real Meta interview question, only consider +, -, no *
    https://www.1point3acres.com/bbs/thread-1039320-1-1.html
    '''
    def addOperators(self, num: str, target: int) -> List[str]:
        pool = []

        def dfs(ni: int, expr: List[str], exprVal: int, lastVal: int):
            '''
            @ni: current index in num
            @expr: current expression
            @exprVal: value of current expression
            @lastVal: last computed value
            '''
            if ni == len(num):
                if exprVal == target:
                    pool.append(''.join(expr))
                return
            
            # Iterate on each integer num[ni : j] 
            for j in range(ni + 1, len(num) + 1):
                newNum = int(num[ni:j])
                newNumStr = str(newNum)
                
                if len(newNumStr) < j - ni:
                    # Example '01', integer will be 1, and then integer string
                    # is '1', which should break, because all later j
                    # will have same issue
                    break
                
                if ni == 0:
                    # Cannot put operator in beginning!
                    dfs(j, [newNumStr], newNum, newNum)
                else:
                    dfs(j, expr + ['+', newNumStr], exprVal + newNum, newNum)
                    dfs(j, expr + ['-', newNumStr], exprVal - newNum, -newNum)
                    dfs(j, expr + ['*', newNumStr], exprVal - lastVal + lastVal * newNum, lastVal * newNum)
        
        dfs(0, [], 0, 0)
        return pool
