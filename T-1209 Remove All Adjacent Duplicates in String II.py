'''
1209. Remove All Adjacent Duplicates in String II
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and
removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
'''
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # [(char, count)]
        for e in s:
            if stack and e == stack[-1][0]:
                ctr = stack[-1][1] + 1
                if ctr == k:
                    stack.pop()
                else:
                    stack[-1] = (e, ctr)
            else:
                stack.append((e, 1))
        
        return ''.join(''.join([e] * c) for e, c in stack)        
