'''
301. Remove Invalid Parentheses
https://leetcode.com/problems/remove-invalid-parentheses/

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:

Input: ")("
Output: [""]
'''
class Solution:
    def minRemoveToMakeValid(self, s: List[str]) -> str:
        '''
        Similar to 1249. Minimum Remove to Make Valid Parentheses
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
                    
    def isValid(self, s: List[str]) -> bool:
        # If a string is valid parentheses paris
        ctr = 0
        for c in s:
            if c == '(': ctr += 1
            elif c == ')': ctr -= 1
            if ctr < 0: return False
        return ctr == 0

    def trim(self, s: List[str]) -> List[str]:
        # Trim off left and right invalid parentheses to speed up.
        size = len(s)
        
        left = 0
        while left < size and s[left] == ')':
            left += 1

        right = size - 1
        while right >= left and s[right] == '(':
            right -= 1
            
        return s[left : right+1]
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        '''
        Optimized BFS
        Time Complexity: maxDepth * N * N
        '''
        ls = self.trim(list(s))
        if self.isValid(ls):
            return [''.join(ls)]

        # Compute how many parentheses needs to be removed.
        # This will be the depth of BFS.
        removeNeeded = self.minRemoveToMakeValid(ls)
        
        queue = collections.deque() # [(string, lastRemovedIndex, lastRemovedChar)]
        queue.append((ls, 0, ')'))
           
        for _ in range(removeNeeded):
            for _ in range(len(queue)):
                node, lastRemovedIndex, lastRemovedChar = queue.popleft()

                # Start from last removal position
                for i in range(lastRemovedIndex, len(node)):
                    c = node[i]
                    if c != '(' and c != ')':
                        continue

                    if i != lastRemovedIndex and c == node[i-1]:
                        # Do not repeatedly remove from consecutive parentheses
                        # Because essentially the removed strings are identical.
                        continue  
                    
                    if lastRemovedChar == '(' and c == ')':
                        # Do not remove a pair of valid parentheses pair.
                        continue
                
                    queue.append((node[:i] + node[i+1:], i, c))
                            
        return [''.join(arr) for arr,_,_ in queue if self.isValid(arr)]
