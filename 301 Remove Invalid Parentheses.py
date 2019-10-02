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
from collections import deque

class Solution:
    def isValid(self, s: List[str]) -> bool:
        # If a string has valid parentheses pairs
        # Notice input is listified str
        ctr = 0
        for ch in s:
            if ch == '(': ctr += 1
            elif ch == ')': ctr -= 1
            if ctr < 0: return False
        return ctr == 0

    def trim(self, ls: List[str]) -> List[str]:
        # Trim off left and right invalid parentheses to speed up the algorithm
        # Notice input is listified str
        length = len(ls)
        
        left = 0
        while left < length and ls[left] == ')':
            left += 1

        right = length - 1
        while right >= left and ls[right] == '(':
            right -= 1
            
        return ls[left : right+1]
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Trim off left and right invalid parentheses to speed up
        ls = self.trim(list(s))
        if self.isValid(ls):
            return [''.join(ls)]

        res = []        
        queue = deque() # [(string, startIndex, lastRemovedChar)]
        queue.append((ls, 0, ')'))
        
        while len(queue):
            node, startIndex, lastRemovedChar = queue.popleft()

            # Start from last removal position
            for i in range(startIndex, len(node)):
                ch = node[i]
                if ch != '(' and ch != ')':
                    continue

                if i != startIndex and node[i-1] == ch:
                    # Do not repeatedly remove from consecutive parentheses
                    # Because essentially the removed strings are all same
                    continue  
                    
                if lastRemovedChar == '(' and ch == ')':
                    # Do not remove a pair of valid parentheses
                    continue
                
                # Remove ch
                child = node[:i] + node[i+1:]
                
                if self.isValid(child):
                    res.append(''.join(child))
                    
                elif len(res) == 0:
                    # If no answer is found yet, add to queue and keep BFS.
                    # Otherwise, no need for next level BFS,
                    # as we only need to remove least amount of parentheses
                    queue.append((child, i, ch));

        return res
