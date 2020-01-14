'''
43. Multiply Strings
https://leetcode.com/problems/multiply-strings/

Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
'''
class Solution:
    def productOfChars(self, c1: str, c2: str) -> int:
        return (ord(c1) - ord('0')) * (ord(c2) - ord('0'))
        
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        # Multiplication result's size is either len(num1) + len(num2) or\
        # len(num1) + len(num2) - 1
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)-1,-1,-1):
            
            carry = 0
            for j in range(len(num2)-1,-1,-1):
                total = res[i+j+1] + self.productOfChars(num1[i], num2[j]) + carry
                res[i+j+1] = total % 10
                carry = total // 10       
            res[i] += carry
    
        if res[0] == 0:
            res = res[1:]
            
        return ''.join(str(i) for i in res)
