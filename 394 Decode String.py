'''
394. Decode String
https://leetcode.com/problems/decode-string/

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''
class Solution:
    def decodeString(self, s: str) -> str:
        '''
        Similar pattern to Calculator question
        '''
        stack = []
        count = 0
        for c in s:
            if c.isdecimal():
                count = count * 10 + int(c)
            elif c.isalpha():
                stack.append(c)
            elif c == '[':
                stack.append(count)
                count = 0
            elif c == ']':
                ls = []
                while stack and isinstance(stack[-1], str):
                    ls.append(stack.pop())
                stack.append(''.join(ls[::-1]) * stack.pop())

        return ''.join(stack)
