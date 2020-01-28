'''
946. Validate Stack Sequences
https://leetcode.com/problems/validate-stack-sequences/

Given two sequences pushed and popped with distinct values,
return true if and only if this could have been the result of a sequence of push and pop operations on
an initially empty stack.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        k = 0 # for popped
        for i, e in enumerate(pushed):
            stack.append(e)
            while stack and stack[-1] == popped[k]:
                stack.pop()
                k += 1
                
        while stack and stack[-1] == popped[k]:
            stack.pop()
            k += 1
        
        return k == len(popped)          
