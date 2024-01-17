'''
301. Remove Invalid Parentheses
https://leetcode.com/problems/remove-invalid-parentheses/

Given a string s that contains parentheses and letters,
remove the minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals.
You may return the answer in any order.

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:

Input: s = ")("
Output: [""]

Constraints:
    1 <= s.length <= 25
    s consists of lowercase English letters and parentheses '(' and ')'.
    There will be at most 20 parentheses in s.
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        Get the minimum remove needed to make the string valid.
        Same as 921. Minimum Add to Make Parentheses Valid
        '''
        invalidLeftBrackets = 0
        invalidRightBrackets = 0
        for c in s:
            if c == '(':
                invalidLeftBrackets += 1
            elif c == ')':
                if invalidLeftBrackets == 0:
                    invalidRightBrackets += 1
                else:
                    invalidLeftBrackets -= 1
        return invalidLeftBrackets + invalidRightBrackets

    def trim(self, s: str) -> List[str]:
        '''
        Trim off left and right invalid parentheses to speed up.
        '''
        size = len(s)  
        left = 0
        while left < size and s[left] == ')':
            left += 1
        right = size - 1
        while right >= left and s[right] == '(':
            right -= 1
        return s[left : right + 1]

    def removeInvalidParentheses(self, s: str) -> List[str]:
        results = []
        visited = set()

        def dfs(ss: str):
            minToRemove = self.minRemoveToMakeValid(ss)
            if minToRemove == 0:
                results.append(ss)
                return
            for i in range(len(ss)):
                if ss[i] in ['(', ')']:
                    # Try remove charList[i] 
                    newSs = ss[:i] + ss[i+1:]
                    if newSs not in visited and self.minRemoveToMakeValid(newSs) < minToRemove:
                        # Go next iteration only if not yet visited and minToRemove is smaller
                        visited.add(newSs)
                        dfs(newSs)

        trimmed = self.trim(s)
        visited.add(trimmed)
        dfs(trimmed)
        return results