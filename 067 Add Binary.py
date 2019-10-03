'''
Add Binary
https://leetcode.com/problems/add-binary/

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"
    
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = [] # list of char bit
        i = len(a) - 1
        j = len(b) - 1
        acc = 0 # carry on 1 bit
        while i > -1 or j > -1 or acc > 0:
            left = ord(a[i]) - ord('0') if i > -1 else 0
            right = ord(b[j]) - ord('0') if j > -1 else 0
            total = left + right + acc
            if total == 0:
                res.append('0')
                acc = 0
            elif total == 1:
                res.append('1')
                acc = 0
            elif total == 2:
                res.append('0')
                acc = 1
            elif total == 3:
                res.append('1')
                acc = 1
            i -= 1
            j -= 1               
        return ''.join(res[::-1])          
